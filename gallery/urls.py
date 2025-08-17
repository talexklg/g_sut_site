from django.urls import path
from .views import AlbumListView, AlbumDetailView

app_name = 'gallery'

urlpatterns = [
    path('', AlbumListView.as_view(), name='album_list'),
    path('<int:pk>/', AlbumDetailView.as_view(), name='album_detail'),
]
