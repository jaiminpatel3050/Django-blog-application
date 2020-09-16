from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostDetails(admin.ModelAdmin):
    list_display= ['title','date_posted','author']