from unicodedata import name
from django.urls import URLPattern, path
from . import views

#creating base app route 
# basically the default for the project 
urlpatterns = [
    path('',views.home,name='home')
    # path('/login',views.login,name='login'),
    # path('/candidate-home',views.candidateHome,name='candidateHome'),
    # path('/recruiter-home',views.recruiterHome,name='recruiterHome')
]