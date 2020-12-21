from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class CommonInfo(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ConsentForm(CommonInfo):
    document = models.FileField(upload_to='consent-form/')


class Fixture(CommonInfo):
    name = models.CharField(max_length=254)
    description = models.TextField(null=True, blank=True)
    picture = models.ImageField(
        upload_to='fixtures/images', null=True, blank=True)
    date = models.DateTimeField()
    starting_players = models.ManyToManyField(User, related_name='fixtures_playing', limit_choices_to={
                                              'role': 'player'}, verbose_name='Starting 11')
    subtitutes = models.ManyToManyField(
        User, related_name='fixtures_subtituting', limit_choices_to={'role': 'player'})
    added_by = models.ForeignKey(
        User, related_name='fixtures_created', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(
        User, related_name='fixtures_updated', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.name} to be held on {self.date}'


class TrainingSession(CommonInfo):
    name = models.CharField(max_length=254)
    description = models.TextField(null=True, blank=True)
    picture = models.ImageField(
        upload_to='traininga/images', null=True, blank=True)
    date = models.DateTimeField()
    players = models.ManyToManyField(
        User, related_name='training_sessions_playing', limit_choices_to={'role': 'player'})
    trainers = models.ManyToManyField(
        User, related_name='training_sesssions_assigned', limit_choices_to={'role': 'trainer'})
    added_by = models.ForeignKey(
        User, related_name='training_sessions_created', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(
        User, related_name='training_sessions_updated', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.name} to be held on {self.date}'
