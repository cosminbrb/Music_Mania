from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.db.models import Count
from .models import Music, Like
from .models import MelodiesToLearn
from .forms import MelodiesToLearnForm

class HomeViewTemplate (TemplateView):
    template_name = 'MusicStoreManager/home.html'


class AlbertViewTemplate (TemplateView):
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


@method_decorator (login_required, name='dispatch')
class LikeMusicView (View):
    def post(self, request, music_id):
        music = get_object_or_404 (Music, id=music_id)
        like, created = Like.objects.get_or_create (user=request.user, music=music)
        if not created:
            like.count += 1
        like.save ()
        return redirect ('music_detail', music_id=music.id)


@method_decorator (login_required, name='dispatch')
class RecommendMusicView (View):
    def get(self, request):
        user_likes = Like.objects.filter (user=request.user)
        user_music_ids = user_likes.values_list ('music_id', flat=True)

        # Find other users who liked the same music
        similar_users = Like.objects.filter (music_id__in=user_music_ids).exclude (user=request.user)

        # Collaborative filtering recommendation system
        recommended_music = (Music.objects
                             .filter (like__in=similar_users)
                             .annotate (num_likes=Count ('like'))
                             .order_by ('-num_likes')
                             .exclude (id__in=user_music_ids))

        return render (request, 'recommendations.html', {'recommended_music': recommended_music})

class AddMelodyView(View):
    def get(self, request):
        form = MelodiesToLearnForm()
        return render(request, 'MusicStoreManager/add_melody.html', {'form': form})

    def post(self, request):
        form = MelodiesToLearnForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'MusicStoreManager/add_melody.html', {'form': form})