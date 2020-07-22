from django.db import models
from django.contrib.auth.models import User

#user profile model

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    gender = models.CharField(max_length=100,default='')
    age  =  models.IntegerField(default=0)
    image  = models.ImageField(upload_to='profile_image',blank=True)
    
    
    def __str__(self):
        return self.user

#ContactUs model

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=250)

    def __str__(self):
        return self.name

#About model

class About(models.Model):
    newsarticle = models.IntegerField()
    reporters = models.IntegerField()
    awardswon = models.IntegerField()
    yearold = models.IntegerField()

position =( 
    ("Reporter", "Reporter"), 
    ("Bureau chief / editor", "Bureau chief / editor"), 
    ("Section editor", "Section editor"), 
    ("Copy editor", "Copy editor"), 
    ("News editor", "News editor"), 
    ("Company lawyer", "Company lawyer"), 
    ("Graphics people", "Graphics people"),    
    ("Stipple portrait artists", "Stipple portrait artists"), 
    ("Company lawyer", "Company lawyer"), 
    ("Online staff", "Online staff"),    
    ("Videographer", "Videographer"), 
    ("Market data group", "Market data group"), 
    ("Library", "Library"),
    ("Deputy managing editor","Deputy managing editor"),
) 

class Employee(models.Model):
    name = models.CharField(max_length=100)
    positions = models.CharField(max_length=25,choices=position)
    image  = models.ImageField(upload_to='employee_prof',blank=True)

    def __str__(self):
        return self.name

#Rest-Framework Model

class category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

class subcategory(models.Model):
    category = models.ForeignKey(category,on_delete=models.CASCADE)
    subcat = models.CharField(max_length=100)

    def __str__(self):
        return self.subcat

class news(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(category,on_delete=models.CASCADE)
    subcat = models.ForeignKey(subcategory,on_delete=models.CASCADE)
    details = models.CharField(max_length=50000,null=True)
    image = models.ImageField(upload_to='news_image')
    date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title

#Comment Model

class Comment(models.Model):
    userid = models.IntegerField()
    newsid = models.IntegerField()
    username = models.CharField(max_length=50)
    userimage = models.ImageField(upload_to='profile_image')
    comments = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.comments

