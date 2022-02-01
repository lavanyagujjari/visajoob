from django.template import Context, loader
from django.shortcuts import render
from django.template.loader import render_to_string
from upload.forms import uploadfileform,uploadImageform
from django import forms
from django.urls import reverse

def uploadfunc(request):
	if request.method=='POST':
		form =uploadfileform(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return render_to_response('upload_successful.html')
	else:
		form=uploadfileform()
	return render(request, 'upload.html',{'form':form})

def uploadImage(request):
	if request.method=='POST':
		form =uploadImageform(request.POST,request.FILES)
		if form.is_valid():
                   print('jiiii')
                   form.save()
		#return render_to_response('upload_successful.html',{'form' : form})
	else:
		form=uploadImageform()
	return render(request, 'upload.html',{'form':form})