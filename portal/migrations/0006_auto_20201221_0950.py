# Generated by Django 3.1.3 on 2020-12-21 06:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portal', '0005_auto_20201220_2041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fixture',
            name='players',
        ),
        migrations.RemoveField(
            model_name='fixture',
            name='trainers',
        ),
        migrations.AddField(
            model_name='fixture',
            name='starting_players',
            field=models.ManyToManyField(limit_choices_to={'role': 'player'}, related_name='fixtures_playing', to=settings.AUTH_USER_MODEL, verbose_name='Starting 11'),
        ),
        migrations.AddField(
            model_name='fixture',
            name='subtitutes',
            field=models.ManyToManyField(limit_choices_to={'role': 'player'}, related_name='fixtures_subtituting', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='TrainingSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField(blank=True, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='traininga/images')),
                ('date', models.DateTimeField()),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='training_sessions_created', to=settings.AUTH_USER_MODEL)),
                ('players', models.ManyToManyField(limit_choices_to={'role': 'player'}, related_name='training_sessions_playing', to=settings.AUTH_USER_MODEL)),
                ('trainers', models.ManyToManyField(limit_choices_to={'role': 'trainer'}, related_name='training_sesssions_assigned', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='training_sessions_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
