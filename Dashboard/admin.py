from django.contrib import admin

from Dashboard.models import Learner, Parent, Feedback, Assignment, Result

admin.site_header = "EduTrack Management"
admin.site.register(Parent)
admin.site.register(Learner)
admin.site.register(Assignment)
admin.site.register(Feedback)
admin.site.register(Result)