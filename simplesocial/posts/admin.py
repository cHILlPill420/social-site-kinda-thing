from django.contrib import admin
from posts import models
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    fields = ['user', 'group', 'message']
    search_fields = ['message','group'] #not for foreignkey therefore for 'group' it wouldn't work
    list_filter = ['group', 'user']
    list_display = ['message', 'group', 'user']
    list_editable = ['user']

admin.site.register(models.Post, PostAdmin)