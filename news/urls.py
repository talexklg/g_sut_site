from django.urls import path
from .views import NewsListView, ContestListView, NewsDetailView, ContestDetailView

app_name = 'news'

urlpatterns = [
    path('', NewsListView.as_view(), name='list'),
    path('contests/', ContestListView.as_view(), name='contest_list'),
    path('<int:pk>/', NewsDetailView.as_view(), name='detail'),
    path('contests/<int:pk>/', ContestDetailView.as_view(), name='contest_detail'),
]
