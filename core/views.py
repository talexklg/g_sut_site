from django.views.generic import TemplateView, ListView
from .models import Achievement

class HomePageView(TemplateView):
    template_name = "home.html"

class AchievementListView(ListView):
    model = Achievement
    template_name = 'core/achievement_list.html'
    context_object_name = 'achievements'