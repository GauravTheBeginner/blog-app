from django.contrib import admin
from .models import BlogPost


@admin.register(BlogPost)
class BlogAdmin(admin.ModelAdmin):
    list_display = []
# Register your models here.
