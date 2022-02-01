"""newProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from tutorial import views
from django.views.generic.base import TemplateView 
from rest_framework import routers

"""oldurl

    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
"""

#router = routers.DefaultRouter()
#router.register(r'restData', views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^special/',views.special,name='special'),
    url(r'tutorial/',include('tutorial.urls')),
    url(r'upload/',include('upload.urls')),
    url(r'admindashboard/',include('admindashboard.urls')),
    path('api/', include('tutorial.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
