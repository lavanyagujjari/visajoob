from django.template import Context, loader
from django.shortcuts import render
from django.template.loader import render_to_string
from tutorial.forms import UserForm
from tutorial.models import UserProfileInfo
from admindashboard.serializers import User_DetailsSerializer,CUser_UpdateSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer

def company_register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid(): 
            user = user_form.save()
            user.is_active = True
            user.mobileno = user_form.cleaned_data.get("mobileno")
            user.userflag = 'C'
            password=user.password
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            return render(request,'registration/companyregistration.html',user_form.errors)
    else:
        user_form = UserForm()
    return render(request,'registration/companyregistration.html',
                          {'user_form':user_form,
                           'registered':registered})

class CUser_DetailsViews(APIView):
    def post(self, request):
        renderer_classes = [TemplateHTMLRenderer]
        template_name = 'admindashboard.html'
        serializer = User_DetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request,*args,**kwargs):
        if request.GET.get("userflag", None) is not None:
           print("the passed attribute:", request.GET["userflag"])
           if request.GET["userflag"]=='C':
                item = UserProfileInfo.objects.get(userflag=request.GET["userflag"])
                serializer = User_DetailsSerializer(item)
                return Response({"status": "success", "data1": serializer.data}, status=status.HTTP_200_OK)
           else:
               items = UserProfileInfo.objects.all()
               serializer = User_DetailsSerializer(items, many=True)
               return Response(serializer.data)

class CUser_Updatestatus(APIView):
    def update(self, request, *args, **kwargs):
      if request.GET.get("id", None) is not None:
        print(request.GET["id"])
        queryset = UserProfileInfo.objects.get(id=request.GET["id"])
        serializer_class = CUser_UpdateSerializer
        permission_classes = (permissions.IsAuthenticated,)
        data_to_change = {'is_staff': True,'admin_status':Y}
        # Partial update of the data
        serializer = self.serializer_class(request.user, data=data_to_change, partial=True)
        if serializer.is_valid():
            self.perform_update(serializer)

        return Response(serializer.data)