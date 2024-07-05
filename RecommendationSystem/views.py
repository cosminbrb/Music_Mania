from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from MusicStoreManager.models import MelodiesToLearn
from .models import Like

@login_required
def like_melody(request, pk):
    melody = get_object_or_404(MelodiesToLearn, pk=pk)
    user = request.user
    Like.objects.get_or_create(user=user, melody=melody)
    return redirect('home.html')
