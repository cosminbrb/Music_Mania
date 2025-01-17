# Generated by Django 5.0.6 on 2024-07-05 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MelodiesToLearn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('style', models.CharField(choices=[('BL', 'Blues'), ('BR', 'Blues Rock'), ('JZ', 'Jazz'), ('PP', 'Pop')], default='BL', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('favorite_melodies', models.ManyToManyField(related_name='fans', to='MusicStoreManager.melodiestolearn')),
            ],
        ),
    ]
