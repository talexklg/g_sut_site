from django.contrib import admin
from .models import Notice

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'is_published')
    list_filter = ('is_published',)
    search_fields = ('title', 'content')