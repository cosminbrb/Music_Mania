from django.db import models

class MelodiesToLearn(models.Model):
    BLUES = 'BL'
    BLUES_ROCK = 'BR'
    JAZZ = 'JZ'
    POP = 'PP'

    STYLE_CHOICES = [
        (BLUES, 'Blues'),
        (BLUES_ROCK, 'Blues Rock'),
        (JAZZ, 'Jazz'),
        (POP, 'Pop'),
    ]

    name = models.CharField(max_length=100)
    style = models.CharField(
        max_length=2,
        choices=STYLE_CHOICES,
        default=BLUES,
    )

    def __str__(self):
        return f'{self.name} - {self.get_style_display()}'

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    favorite_melodies = models.ManyToManyField(MelodiesToLearn, related_name='fans')

    def __str__(self):
        return self.name
