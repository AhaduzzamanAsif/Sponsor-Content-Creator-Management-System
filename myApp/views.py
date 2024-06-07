from typing import Any
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib import messages
from .models import Post
from django.conf import settings
from .models import *

from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth import logout





# Create your views here.

def index(request):
    if request.method=="POST":
        user = User.objects.get(username=request.user)
        Description = request.POST['description']
        f1 = Post(user=user,Description=Description)
        f1.save()

    posts = list(Post.objects.all())
    posts.reverse()

    
    
    return render (request,'index.html', {'posts':posts})

def registration(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        usertype =request.POST['user_type']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Used')
                return redirect('register')
            else:

                if usertype == 'contentcreator':
                    user = User.objects.create_user(username=username,email=email,password=password)
                    ContentCreator.objects.create(user=user)
                elif usertype == 'sponsor':
                    user = User.objects.create_user(username=username,email=email,password=password)
                    Sponsor.objects.create(user=user)

                return redirect('register')
        else:
            messages.info(request,'Password not same')
            return redirect('register')
    else:
        return render(request,'register.html')
    
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Credentials Invalid')
            return redirect('login')
    return render(request,'login.html')

def registerPage(request):
    form = CreateUserForm()
    

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            cc = ContentCreator.objects.create(user=user)
            cc.save()

    context ={'form':form}
    return render(request,'registrationform.html',context)

def profile(request):
    user = User.objects.get(username=request.user)
    cc = ContentCreator.objects.filter(user=user).first
    bidmessages = None
    if ContentCreator.objects.filter(user = user).exists()==True:
        cc1 = ContentCreator.objects.get(user=user)
        bidmessages = BidMessage.objects.filter(user=cc1)
    #, 'cc':cc, 'bidmessages':bidmessages
    
    return render(request, 'profile.html',{'userinfo':user, 'cc':cc, 'bidmessages':bidmessages})

def logout_view(request):
    logout(request)
    return redirect('/')

def updateProfile(request,pk):
    user = User.objects.get(id=pk)
    form = UpdateProfile(instance=user)
    if request.method == 'POST':
        form = UpdateProfile(request.POST,request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/')


    return render(request, 'updateprofile.html',{'form':form})

def upadateBprofile(request,pk):
    user = User.objects.get(id=pk)
    userp = ContentCreator.objects.get(user=user)
    form = UpdateBusinessProfile(instance=userp)
    if request.method == 'POST':
        form = UpdateBusinessProfile(request.POST,request.FILES, instance=userp)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    return render(request, 'updateBprofile.html',{'form':form})

def ccdashboard(request):
    cc = ContentCreator.objects.all()
    return render(request, 'ccdashboard.html',{'cc':cc})


def ccdetail(request,pk):
    user = User.objects.get(id=pk)
    cc = ContentCreator.objects.get(user=user)
    user1 = User.objects.get(username=request.user)
    flag = 0
    if Sponsor.objects.filter(user=user1).exists():
        flag = 1
    if request.method == 'POST':
        sp = Sponsor.objects.get(user=user1)
        companyName = request.POST['companyName']
        bidAmount = request.POST['bidAmount']
        message = request.POST['message']
        msg = "Sponsor Name: "+sp.user.username+"\nCompany Name: "+companyName+"\nBid Amount: "+bidAmount+"\nMessage: "+message
        BidMessage.objects.create(user=cc,user1=sp,bidmessage=msg)

    return render(request, 'ccdetail.html',{'cc':cc,'flag':flag})


def createConversation(request,pk):
    user = User.objects.get(id=pk)
    sp = Sponsor.objects.get(user=user)
    user1 = User.objects.get(username=request.user)
    cc = ContentCreator.objects.get(user=user1)
    bidToDelete = BidMessage.objects.filter(user=cc, user1=sp)
    bidToDelete.delete()
    Chatroom.objects.create(cc=cc,sp=sp,msg="Now You can communicate")
    return redirect('/')

def Chatrooms(request):
    user = User.objects.get(username=request.user)
    chatrooms = None
    flag = 0
    if ContentCreator.objects.filter(user=user).exists():
        cc = ContentCreator.objects.get(user=user)
        chatrooms = Chatroom.objects.filter(cc=cc)
        flag = 1
    else:
        sp = Sponsor.objects.get(user=user)
        chatrooms = Chatroom.objects.filter(sp=sp)
    return render(request, 'chatroom.html',{'chatrooms':chatrooms,'flag':flag})

def Conversation(request,pk):
    chat_room = Chatroom.objects.get(id=pk)
    messages = Message.objects.filter(chat_room=chat_room)
    user = User.objects.get(username=request.user)
    flag = 0
    if Sponsor.objects.filter(user=user).exists():
        flag = 1
    if 'msg' in request.POST:
        message = request.POST['message']
        Message.objects.create(chat_room=chat_room,author=user,msg=message)
    elif 'amt' in request.POST:
        amount = request.POST['amount']
        chat_room.amount = amount
        chat_room.save()
    elif 'content' in request.POST:
        link = request.POST['link']
        chat_room.contentLink = link
        chat_room.save()
    elif 'approve' in request.POST:
        chat_room.isSpApproved = True
        chat_room.save()
    return render(request, 'conversation.html',{'messages':messages,'flag':flag,'cr':chat_room})

