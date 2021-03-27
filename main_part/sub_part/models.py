from django.db import models

# Create your models here.
class adminsdb(models.Model):
    firstname=models.CharField(max_length=30, default='Type here')
    lastname=models.CharField(max_length=30, default='Type here')
    email=models.CharField(max_length=30, default='Type here')
    phone=models.CharField(max_length=30, default='Type here')
    username=models.CharField(max_length=30, default='Type here')
    password=models.CharField(max_length=30, default='Type here')
    address=models.CharField(max_length=30, default='Type here')

    def __str__(self):
        return self.firstname


class addpreregdb(models.Model):
    firstname=models.CharField(max_length=30, default='Type here')
    lastname=models.CharField(max_length=30, default='Type here')
    email=models.CharField(max_length=30, default='Type here')
    phone=models.CharField(max_length=30, default='Type here')
    gender=models.CharField(max_length=30, default='Type here')
    emp=models.CharField(max_length=30, default='Type here')
    date=models.CharField(max_length=30, default='Type here')
    time=models.CharField(max_length=30, default='Type here')
    comment=models.CharField(max_length=30, default='Type here')
    address=models.CharField(max_length=30, default='Type here')

    def __str__(self):
        return self.firstname


    class Meta: 

     db_table = "addpreregform"


class addvisitorsdb(models.Model):
    firstname=models.CharField(max_length=30, default='Type here')
    lastname=models.CharField(max_length=30, default='Type here')
    email=models.CharField(max_length=30, default='Type here')
    phone=models.CharField(max_length=30, default='Type here')
    gender=models.CharField(max_length=30, default='Type here')
    companyname=models.CharField(max_length=30, default='Type here')
    idnumber=models.CharField(max_length=30, default='Type here')
    emp=models.CharField(max_length=30, default='Type here')
    purpose=models.CharField(max_length=30, default='Type here')
    address=models.CharField(max_length=30, default='Type here')

    def __str__(self):
        return self.firstname

    

class addrolesdb(models.Model):
    name=models.CharField(max_length=30, default='Type here')
    
    def __str__(self):
        return self.name

class usersignupdb(models.Model):
    name=models.CharField(max_length=30, default='Type here')
    email=models.CharField(max_length=30, default='Type here')
    username=models.CharField(max_length=30, default='Type here')
    password=models.CharField(max_length=30, default='Type here')

    def __str__(self):
        return self.name