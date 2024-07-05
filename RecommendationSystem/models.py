from django.db import models
from MusicStoreManager.models import MelodiesToLearn
from django.contrib.auth import get_user_model

User = get_user_model()

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    melody = models.ForeignKey(MelodiesToLearn, on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} liked {self.melody.name}'
