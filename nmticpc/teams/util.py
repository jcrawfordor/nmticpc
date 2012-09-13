from teams.models import TeamProfile, Problem, Submission

def getRankedTeams():
    """ Gets a list of vital team info ranked by their scores """
    # First, get a list of all teams.
    teamlist = TeamProfile.objects.filter(user__is_staff=False)

    # we rebuild the entire list. Not awesome for memory, but easy.
    newlist = []
    for team in teamlist:
        newlist.append({'name': team.user.username, 'score': team.getScore(), 'mugshot': team.get_mugshot_url()})

    newlist.sort(key=lambda x: x['score'], reverse=True)

    return newlist

from datetime import datetime
from django.conf import settings
def isCompetitionLive():
    """ Returns true if the competition has started AND not ended yet. """
    if datetime.now() > settings.COMPETITION_START_TIME and datetime.now() <= settings.COMPETITION_END_TIME:
        return True
    else:
        return False
