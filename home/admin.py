from django.contrib import admin

# Register your models here.
from .models import Videos


class VideosAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'created_at')


admin.site.register(Videos, VideosAdmin)
