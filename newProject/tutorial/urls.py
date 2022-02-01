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

from django.urls import path
from django.conf.urls import url
from . import views 
from tutorial.views import CartItemViews
from admindashboard.views import CUser_DetailsViews,CUser_Updatestatus
from django.conf import settings
from django.conf.urls.static import static
#path('',views.homepage, name="homepage"),

app_name="tutorial"
urlpatterns = [
    url(r'^register/$',views.register,name='register'),
    url(r'^mobile_data/$',views.mobile_data,name='mobile_data'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^rest_data/$',views.restData,name='rest_data'),
    url(r'^index_data/$',views.index_data,name='index_data'),
    path('cart-items/', CartItemViews.as_view()),
    path('cart-items/<int:id>', CartItemViews.as_view()),
    path('user_Details/', CUser_DetailsViews.as_view()),
    path('user_Details/<str:userflag>/', CUser_DetailsViews.as_view()),
    path('CUser_Updatestatus/<int:id>/', CUser_Updatestatus.as_view())
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()
