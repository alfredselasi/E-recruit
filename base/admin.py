from django.contrib import admin
from .models import Candidate,Recruiter,Candidate_Applications,Recruiter_Job

# Register your models here.

admin.site.register(Candidate)
admin.site.register(Recruiter)
admin.site.register(Recruiter_Job)
admin.site.register(Candidate_Applications)

