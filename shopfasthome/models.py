from django.db import models

# Create your models here.

class uppdernavimages(models.Model):
    name = models.CharField( max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to='pics')

class contactUs(models.Model):
    firstName=models.CharField(max_length=50)
    lastName=models.CharField(max_length=50)
    emailId=models.CharField(max_length=50)
    commentUser=models.CharField(max_length=500)

class feedbackForm(models.Model):
    ratings=models.IntegerField(max_length=5)
    experience=models.CharField(max_length=500)
    suggestion=models.CharField(max_length=500)