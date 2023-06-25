from django.contrib import admin
from blog.models import Post

# Register your models here.
@admin.register(Post)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display=['pk','title','date','author','text', 'show']