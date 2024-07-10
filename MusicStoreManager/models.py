from django.db import models

class MelodiesToLearn(models.Model):
    STYLE_CHOICES = [
        ('BL', 'Blues'),
        ('BR', 'Blues Rock'),
        ('JZ', 'Jazz'),
        ('PP', 'Pop'),
    ]

    name = models.CharField(max_length=100)
    style = models.CharField(
        max_length=2,
        choices=STYLE_CHOICES,
        default='BL',
    )

    def __str__(self):
        return f'{self.name} - {self.get_style_display()}'

class Music(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} by {self.artist}'

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    favorite_melodies = models.ManyToManyField(MelodiesToLearn, related_name='fans')

    def __str__(self):
        return self.name

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'music')

    def __str__(self):
        return f'{self.user.name} liked {self.music.title}'
