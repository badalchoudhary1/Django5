from django.db import models
from django.contrib.auth.models import User


class Song(models.Model):
    user = models.ManyToManyField(User)
    title = models.CharField(max_length=100)

    def written_by(self):
        return "," .join([str(p) for p in self.user.all()])
