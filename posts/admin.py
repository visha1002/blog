from django.contrib import admin
from .models import Post

# Register your models here.

class showpost(admin.ModelAdmin):
    list_display = ['title', 'body', 'created_at']

admin.site.register(Post, showpost)