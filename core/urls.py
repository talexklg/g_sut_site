from django.urls import path
from .views import HomePageView, AchievementListView

app_name = 'core'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('achievements/', AchievementListView.as_view(), name='achievement_list'),
]
