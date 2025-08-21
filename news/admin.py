from django.contrib import admin
from .models import NewsArticle, Contest

@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'is_published')
    list_filter = ('is_published', 'author')
    search_fields = ('title', 'content')
    date_hierarchy = 'pub_date'
    
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'author', 'is_published')
        }),
        ('Изображение', {
            'classes': ('collapse',),
            'description': 'Загрузите файл или укажите ссылку. Что-то одно.',
            'fields': ('image', 'image_url'),
        }),
        ('Видео', {
            'classes': ('collapse',),
            'description': 'Загрузите файл или укажите ссылку. Что-то одно.',
            'fields': ('video', 'video_url'),
        }),
    )

@admin.register(Contest)
class ContestAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')

    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'start_date', 'end_date', 'is_active')
        }),
        ('Изображение', {
            'classes': ('collapse',),
            'description': 'Загрузите файл или укажите ссылку. Что-то одно.',
            'fields': ('image', 'image_url'),
        }),
        ('Видео', {
            'classes': ('collapse',),
            'description': 'Загрузите файл или укажите ссылку. Что-то одно.',
            'fields': ('video', 'video_url'),
        }),
    )
