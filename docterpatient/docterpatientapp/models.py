from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key= True)
    fname = models.CharField(max_length = 122)
    lname = models.CharField(max_length = 122)
    profile_image = models.ImageField(upload_to= "upload/", max_length= 122, blank= True, default= None)
    username = models.CharField(max_length = 122)
    email = models.EmailField()
    password = models.CharField(max_length = 122)
    userType = models.BooleanField()  # 0 Patient 1 Doctor
    address = models.CharField(max_length = 122)
    city = models.CharField(max_length = 122)
    state = models.CharField(max_length = 122)
    pincode = models.IntegerField(max_length = 122)

    def __str__(self):
        return self.id
    