from django.db import models
#from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from datetime import datetime
from django.contrib.auth.models import AbstractUser



# Create your models here.

class User(AbstractUser):
    is_contentCreator = models.BooleanField(default=False)
    is_sponsor = models.BooleanField(default=False)
    phone=models.CharField(max_length=200, blank=True)
    image = models.ImageField(null=True, blank=True)

class ContentCreator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    channelname = models.CharField(max_length=200, blank=True)
    total_subscriber = models.CharField(max_length=200, blank=True)
    description = models.TextField(null=True,blank=True)
    about = models.TextField(null=True,blank=True)
    contactinfo = models.TextField(null=True,blank=True)
    contentstyle = models.TextField(null=True,blank=True)
    image = models.ImageField(null=True, blank=True)
    publish = models.BooleanField(default=False)


    def __str__(self):
    	return self.user.username





class Sponsor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    organizationname = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
    	return self.user.username
    

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    Description = models.TextField(null=True,blank=True)
    create_at = models.DateTimeField(default=datetime.now, blank=True)

class BidMessage(models.Model):
    user = models.ForeignKey(ContentCreator, on_delete=models.SET_NULL,null=True)
    user1 = models.ForeignKey(Sponsor, on_delete=models.SET_NULL,null=True)
    bidmessage = models.TextField(null=True,blank=True)

class Chatroom(models.Model):
    cc = models.ForeignKey(ContentCreator, on_delete=models.SET_NULL,null=True)
    sp = models.ForeignKey(Sponsor, on_delete=models.SET_NULL,null=True)
    msg = models.TextField(null=True,blank=True)
    create_at = models.DateTimeField(default=datetime.now, blank=True)
    amount = models.CharField(max_length=200, blank=True)
    contentLink = models.TextField(null=True,blank=True)
    transactionID = models.TextField(null=True,blank=True)
    isSpApproved = models.BooleanField(default=False)
    isAdApproved = models.BooleanField(default=False)

class Message(models.Model):
    chat_room = models.ForeignKey(Chatroom, on_delete=models.SET_NULL,null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    msg = models.TextField(null=True,blank=True)
    create_at = models.DateTimeField(default=datetime.now, blank=True)





