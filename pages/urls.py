from django.urls import path
from .views import ContactsPageView, HistoryPageView, OfficialInfoPageView, SummerCampPageView, SafetyPageView

app_name = 'pages'

urlpatterns = [
    path('contacts/', ContactsPageView.as_view(), name='contacts'),
    path('history/', HistoryPageView.as_view(), name='history'),
    path('official-info/', OfficialInfoPageView.as_view(), name='official_info'),
    path('summer-camp/', SummerCampPageView.as_view(), name='summer_camp'),
    path('safety/', SafetyPageView.as_view(), name='safety'),
]
