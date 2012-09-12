from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from userena.models import UserenaBaseProfile

class TeamProfile(UserenaBaseProfile):
    user = models.OneToOneField(User, unique=True, verbose_name=('user'), related_name='team_profile')
    def __unicode__(this):
        return this.user.username

class Problem(models.Model):
    number = models.IntegerField()
    value  = models.IntegerField()

    def __str__(this):
        return str(this.number)

class Submission(models.Model):
    author = models.ForeignKey(TeamProfile)
    problem = models.ForeignKey(Problem)
    reviewed = models.BooleanField()
    valid = models.BooleanField()
    comment = models.TextField()
    content = models.FileField(upload_to="submissions/%Y-%m-%d-%H%M%S")
    submitted = models.DateTimeField(auto_now_add = True)
