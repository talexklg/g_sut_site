from django.contrib import admin
from .models import Album, Photo, Video # Import Video

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1  # Number of extra forms to display

class VideoInline(admin.TabularInline):
    model = Video
    extra = 1

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, VideoInline] # Add VideoInline
    list_display = ('title', 'created_at')
    search_fields = ('title',)

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'album', 'uploaded_at')
    list_filter = ('album',)
    search_fields = ('title', 'album__title')

@admin.register(Video) # Register Video model
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'album', 'uploaded_at')
    list_filter = ('album',)
    search_fields = ('title', 'album__title')