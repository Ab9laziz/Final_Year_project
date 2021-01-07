from django.db import models

# Create your models here.

class CommonInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Blog(CommonInfo):
    title = models.CharField(max_length=254)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title