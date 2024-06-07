from django.urls import path
from .import views

urlpatterns = [
    path('',views.ccdashboard,name='ccdashboard'),
    path('register',views.registration,name='register'),
    path('login',views.login,name='login'),
    path('registrationform',views.registerPage,name='registrationform'),
    path('profile',views.profile,name='profile'),
    path('logout_view/', views.logout_view, name="logout_view"),
    path('updateprofile/<str:pk>/',views.updateProfile,name='updateprofile'),
    path('updateBprofile/<str:pk>/',views.upadateBprofile,name='updateBprofile'),
    path('ccdetail/<str:pk>/',views.ccdetail,name='ccdetail'),
    path('profile/<str:pk>/',views.createConversation,name='createConversation'),
    path('Chatrooms',views.Chatrooms,name='Chatrooms'),
    path('Conversation/<str:pk>/',views.Conversation,name='Conversation'),
]