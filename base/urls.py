from unicodedata import name
from django.urls import URLPattern, path
from . import views

#creating base app route 
# basically the default for the project 
urlpatterns = [
    path('',views.home,name='Home'),
    path('home',views.home, name="Home"),
    path('candidate/login',views.candidateLogin,name='Candidate Login'),
    path('recruiter/login',views.recruiterLogin, name='Recruiter Login'),
    path('candidate/home',views.candidateHome,name="Candidate Home"),
    path('recruiter/home',views.recruiterHome,name="Recruiter Home"),
    path('candidate/register',views.registerCandidate,name="Register Candidate"),
    path('recruiter/register',views.registerRecruiter,name="Register Recruiter"),
    path('recruiter/view/job/<int:job_id>',views.viewJob,name='viewJob'),
    path('candidate/view/job/<int:job_id>',views.viewJob,name='viewJob'),
    path('candidate/apply/job/<int:job_id>',views.applyJob,name='applyJob'),
    path('logout',views.logout,name="logout"),
    path('recruiter/post/job',views.postJob,name='postJob'),
    path('success',views.successPage,name="success"),
    path('fail',views.failPage,name="fail"),
    path('error',views.errorPage,name="error")
    # path('/candidate-home',views.candidateHome,name='candidateHome'),
    # path('/recruiter-home',views.recruiterHome,name='recruiterHome')
]