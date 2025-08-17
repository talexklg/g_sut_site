from django.views.generic import TemplateView

class ContactsPageView(TemplateView):
    template_name = "pages/contacts.html"

class HistoryPageView(TemplateView):
    template_name = "pages/history.html"

class OfficialInfoPageView(TemplateView):
    template_name = "pages/official_info.html"

class SummerCampPageView(TemplateView):
    template_name = "pages/summer_camp.html"

class SafetyPageView(TemplateView):
    template_name = "pages/safety.html"