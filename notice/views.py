from django.views.generic import ListView, DetailView
from .models import Notice

class NoticeListView(ListView):
    model = Notice
    template_name = 'notice/notice_list.html'
    context_object_name = 'notices'
    queryset = Notice.objects.filter(is_published=True)

class NoticeDetailView(DetailView):
    model = Notice
    template_name = 'notice/notice_detail.html'
    context_object_name = 'notice'