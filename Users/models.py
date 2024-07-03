from django.db import models
from MusicStoreManager.models import MelodiesToLearn

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    favorite_melody = models.ForeignKey(MelodiesToLearn, on_delete=models.CASCADE, related_name='users')

    def __str__(self):
        return self.name
