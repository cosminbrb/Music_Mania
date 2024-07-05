from django.urls import path
from .views import like_melody

urlpatterns = [
    path ('like/<int:pk>/', like_melody, name='like-melody'),
]