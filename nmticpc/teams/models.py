from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from userena.models import UserenaBaseProfile

class TeamProfile(UserenaBaseProfile):
    user = models.OneToOneField(User, unique=True, verbose_name=('user'), related_name='team_profile')

class Problem(models.Model):
    number = models.IntegerField()
    value  = models.IntegerField()

class Submission(models.Model):
    team = models.ForeignKey(TeamProfile)
    author = models.ForeignKey(Problem)
    reviewed = models.BooleanField()
    valid = models.BooleanField()
    comment = models.TextField()
    content = models.FileField(upload_to="/submissions/%Y-%m-%d-%H%M%S")
