from django.views.generic import ListView, DetailView
from .models import Album, Photo, Video

class AlbumListView(ListView):
    model = Album
    template_name = 'gallery/album_list.html'
    context_object_name = 'albums'

class AlbumDetailView(DetailView):
    model = Album
    template_name = 'gallery/album_detail.html'
    context_object_name = 'album'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        album = self.get_object()
        context['photos'] = album.photos.all()
        context['videos'] = album.videos.all()
        return context