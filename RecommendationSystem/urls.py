from django.urls import path
from .views import LikeMelodyView

urlpatterns = [
    path('like/<int:pk>/', LikeMelodyView.as_view(), name='like_melody'),
]
