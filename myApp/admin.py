from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Post)
admin.site.register(User)
admin.site.register(ContentCreator)
admin.site.register(Sponsor)
admin.site.register(BidMessage)
admin.site.register(Chatroom)
admin.site.register(Message)