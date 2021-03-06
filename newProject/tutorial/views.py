# from django.shortcuts import HttpResponse

# def homepage(request):
#    return HttpResponse("First App")

from django.template import Context, loader
from django.shortcuts import render
from django.template.loader import render_to_string
from tutorial.forms import UserForm,DataForm #,UserProfileInfoForm
from tutorial.models import login_det
from tutorial.models import data_form,rest_form,UserProfileInfo
from tutorial.serializers import UserSerializer
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from upload.forms import uploadfileform,uploadImageform
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
import pywhatkit
import requests

def index(request):
    return render(request,'registration/index.html')

def index_data(request):
#    login_details = login_det.objects.values_list('dept_name','dept_code','mobile').get(dept_name__exact = 'Cochin')
#    print(login_details)
#    tmpl = loader.get_template("registration/index_data.html")
#    ctx = {'data_detail': login_details}
#    return HttpResponse(tmpl.render(ctx))

     return render(request,'registration/index_data.html',{'data_detail' : login_det.objects.all()})

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    url = "https://www.fast2sms.com/dev/bulk"
    headers = {'authorization': "LJrzY5egvKV7sZquQWNbGaEoTdOCjp2lk4D8h9UBnywFc0P3xRrkKATH605wQjCDNWge9SaBthRbXnc8",'Content-Type': "application/x-www-form-urlencoded",'Cache-Control': "no-cache",}
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        # profile_form = UserProfileInfoForm(data=request.POST) downn line and profile_form.is_valid():
        if user_form.is_valid(): 
            user = user_form.save()
            user.is_active = True
            user.mobileno = user_form.cleaned_data.get("mobileno")
            password=user.password
            user.set_password(user.password)
            user.save()
            payload = "sender_id=FSTSMS&message=login Credentials  "+user.username+"/"+password+"&language=english&route=p&numbers=8790383683"
            response = requests.request("POST", url, data=payload, headers=headers)
            print(response.text)
            # profile = profile_form.save(commit=False)
            # profile.user = user
            # if 'profile_pic' in request.FILES:
            #    print('found it')
            #    profile.profile_pic = request.FILES['profile_pic']
            # profile.save()
            registered = True
        else:
            print(user_form.errors)#,profile_form.errors)
    else:
        user_form = UserForm()
        # profile_form = UserProfileInfoForm()
    return render(request,'registration/registration.html',
                          {'user_form':user_form,
                           #'profile_form':profile_form,
                           'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        UserProfileInfo = authenticate(username=username, password=password)
        if UserProfileInfo:
            if UserProfileInfo.is_active:
               if username=='admin':
                  login(request,UserProfileInfo)
                  return render(request, 'registration/admindashboard.html')
               else:
                  login(request,UserProfileInfo)
                  return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'registration/login.html', {})

def mobile_data(request):
    if request.method == 'POST':
       image_obj
       data_form = DataForm(data=request.POST)
       image_form = uploadImageform(request.POST,request.FILES)
       if data_form.is_valid():data_form.save()
       else:print(data_form.errors)
       try:
          if image_form.is_valid():
             image_form.save()
             image_obj=image_form.instance
       except:
          return render(request, 'registration/mobile_data.html',{'image_form':image_form,'img_obj':image_obj})
    else:
       data_form=DataForm()
       #form=uploadfileform()
       form=uploadImageform()
    return render(request, 'registration/mobile_data.html', {'mobile_data':data_form,'upload_form':form})

class CartItemViews(APIView):
    def post(self, request):
        renderer_classes = [TemplateHTMLRenderer]
        template_name = 'Rest_data.html'
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            item = rest_form.objects.get(id=id)
            serializer = UserSerializer(item)
            return Response({"status": "success", "data1": serializer.data}, status=status.HTTP_200_OK)

        items = rest_form.objects.all()
        serializer = UserSerializer(items, many=True)
        #pywhatkit.sendwhatmsg("+919966506863","Hi",16,22)
        return Response(serializer.data)
        #return HttpResponse(serializer.data)

def restData(request):
    return render(request, 'registration/rest_data.html')