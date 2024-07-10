from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from .models import MelodiesToLearn, Like

@method_decorator(login_required, name='dispatch')
class LikeMelodyView(View):
    def post(self, request, pk):
        melody = get_object_or_404(MelodiesToLearn, pk=pk)
        user = request.user
        Like.objects.get_or_create(user=user, melody=melody)
        return redirect('home.html')

    def get(self, request, pk):
        return self.post(request, pk)
