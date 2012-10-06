NMTICPC
=======

*The retrospectively stupidly named competition framework*

NMTICPC is a Django-based web application for running manually-judged computer programming competitions in the style of the ACM International Collegiate Programming Competition.

It has several features:

1.  Live scoreboard with live elapsed/remaining time display
2.  Solution submission interface that shows submission history and a problem status overview
3.  Django admin configured for easy use by judges

And several limitations:

1.  Problems are expected to be distributed on paper or by other means, right now NMTICPC isn't set up to host the actual problem descriptions
2.  The scoreboard doesn't do any kind of tie resolution, this will need to be done by hand if necessary
3.  Judges just use the django admin interface, which is not the most polished way to do things
3.  The whole thing was put together pretty quickly, so YMMV

NMTICPC was originally developed by Jesse B. Crawford (<jcrawford@cs.nmt.edu>) for the New Mexico Tech Programming Club's ICPC practice events. It was intended for one-time use only, but then got posted on github and reused.

Setup
-----

*  Obviously, you'll need an environment to run Django. NMTICPC was developed for Django 1.4 on Ubuntu 12.04 served via Apache. It should work on other environments as well.
*  In nmticpc/, edit settings.py for your database environment (you made a database already, right?) and run `./manage.py syncdb`. When asked to create a superuser account, do so.
*  Run `./manage.py check_permissions` to add proper Userena permissions to the superuser account.
*  Make a directory `<reporoot>/static` and run `./manage.py collectstatic` to accumulate static files there
*  Make a directory `<reporoot>/media` and ensure that the webserver can write it
*  Apache (or whatever server you use) should be configured to serve `/static/` from `<reporoot>/static` and `/media/` from `<reporoot>/media` (if you change the relative path to these directories, change it in settings.py)
*  Start up your webserver, go to /admin, and log in. Create a problem object for each problem.
*  Set the competition start and end times appropriately at the bottom of settings.py.

Usage
-----

*  Have teams or competitors register accounts before the event.
*  Then, teams can submit solutions fairly intuitively (via the Problems tab and then clicking on individual problems).
*  Judges log in to the admin interface and select Submissions. Click on each submission and click on the file name to download it, then check "Valid" if it's correct and "Reviewed" either way (so that you know it's been scored already). Add a comment if you'd like and then save your changes to the object. 
*  And that's basically it.
