from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from userena.models import UserenaBaseProfile

class TeamProfile(UserenaBaseProfile):
    user = models.OneToOneField(User, unique=True, verbose_name=('user'), related_name='team_profile')
    def __unicode__(this):
        return this.user.username

    def getScore(this):
        problemlist = Problem.objects.all()
        score = 0
        for problem in problemlist:
            if problem.isSolvedBy(this.user):
                score += 1
        return score

class Problem(models.Model):
    number = models.IntegerField()
    value  = models.IntegerField()

    def __str__(this):
        return str(this.number)

    def isSolvedBy(this, team):
        """ Given a TeamProfile object, determines if they have solved this problem or not """
        validsubmissions = Submission.objects.filter(problem=this,author=team,valid=True)
        if len(validsubmissions) > 0:
            return True
        else:
            return False

class Submission(models.Model):
    author = models.ForeignKey(User)
    problem = models.ForeignKey(Problem)
    reviewed = models.BooleanField()
    valid = models.BooleanField()
    comment = models.TextField(blank=True)
    content = models.FileField(upload_to="submissions/%Y-%m-%d-%H%M%S")
    submitted = models.DateTimeField(auto_now_add = True)
