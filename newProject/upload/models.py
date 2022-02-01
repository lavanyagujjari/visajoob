from django.db import models

class uploadfolder(models.Model):
    """ my application """
    File = models.FileField(upload_to='')

class uploadImage(models.Model):
   File = models.ImageField(upload_to='images')
