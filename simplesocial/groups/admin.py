from django.contrib import admin
from groups import models

# Register your models here.

#since Group is parent class of GroupMember inline class will help to access child class from the same page as parent class or something like that
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)