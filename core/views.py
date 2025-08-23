from django.views.generic import TemplateView, ListView
from .models import Achievement
from django.shortcuts import render
from django.db.models import Q
from news.models import NewsArticle

class HomePageView(TemplateView):
    template_name = "home.html"

class AchievementListView(ListView):
    model = Achievement
    template_name = 'core/achievement_list.html'
    context_object_name = 'achievements'

def search_results(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = NewsArticle.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )

    return render(request, 'search_results.html', {
        'query': query,
        'results': results
    })