from django.db import models

TYPES = (
    ("fantasy", "Opowiadanie Fantasy"),
    ("erotic","Opowiadanie Erotyczne"),
)

# Create your models here.
class Story(models.Model):
    title = models.CharField(max_length=128)
    type = models.CharField(max_length=64, choices=TYPES)
    plot = models.TextField()
    publication_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title