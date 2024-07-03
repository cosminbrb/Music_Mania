from django.views.generic import TemplateView


# Create your views here.
class HomeViewTemplate (TemplateView):
    template_name = 'MusicStoreManager/home.html'
class AlbertViewTemplate(TemplateView):
    template_name = 'MusicStoreManager/albert.html'

class BBViewTemplate (TemplateView):
    template_name = 'MusicStoreManager/bb.html'

class BethViewTemplate (TemplateView):
    template_name = 'MusicStoreManager/beth.html'

class BuddyViewTemplate (TemplateView):
    template_name = 'MusicStoreManager/buddy.html'

class ChristoneViewTemplate (TemplateView):
    template_name = 'MusicStoreManager/christone.html'

class EricViewTemplate (TemplateView):
    template_name = 'MusicStoreManager/eric.html'

class HowToPlayViewTemplate (TemplateView):
    template_name = 'MusicStoreManager/howtoplay.html'

class JoeViewTemplate (TemplateView):
    template_name = 'MusicStoreManager/joe.html'

class SRVViewTemplate (TemplateView):
    template_name = 'MusicStoreManager/srv.html'

class SusanViewTemplate (TemplateView):
    template_name = 'MusicStoreManager/susan.html'
