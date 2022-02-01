from upload.models import uploadfolder,uploadImage
from django import forms

class uploadfileform(forms.ModelForm):
	class Meta:
		model=uploadfolder
		fields=('File',)

class uploadImageform(forms.ModelForm):
	class Meta:
		model=uploadImage
		fields=('File',)