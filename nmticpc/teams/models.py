from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from userena.models import UserenaBaseProfile

class TeamProfile(UserenaBaseProfile):
    user = models.OneToOneField(User, unique=True, verbose_name=('user'), related_name='team_profile')
    
