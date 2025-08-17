from django.views.generic import ListView, DetailView
from .models import NewsArticle, Contest

class NewsListView(ListView):
    model = NewsArticle
    template_name = 'news/news_list.html'
    context_object_name = 'news_articles'
    queryset = NewsArticle.objects.filter(is_published=True)

class ContestListView(ListView):
    model = Contest
    template_name = 'news/contest_list.html'
    context_object_name = 'contests'
    queryset = Contest.objects.filter(is_active=True)

class NewsDetailView(DetailView):
    model = NewsArticle
    template_name = 'news/news_detail.html'
    context_object_name = 'news_article'

class ContestDetailView(DetailView):
    model = Contest
    template_name = 'news/contest_detail.html'
    context_object_name = 'contest'