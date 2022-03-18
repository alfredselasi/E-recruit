import email
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# Recruiter table
class Recruiter(models.Model): 
    email=models.EmailField(null=False,blank=False)
    first_name=models.CharField(max_length=50,null=False,blank=False)
    last_name=models.CharField(max_length=50,null=False,blank=False)
    company_name=models.CharField(max_length=50,null=False,blank=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    phone_number = models.CharField(max_length=10,null=False,blank=False)
    date_modified = models.DateTimeField(auto_now=True)
    date_created =  models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.company_name

# Candidate Table 
class Candidate(models.Model):
    email=models.EmailField(null=False,blank=False)
    first_name=models.CharField(max_length=50,null=False,blank=False)
    last_name=models.CharField(max_length=50,null=False,blank=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    work_history = models.TextField(null=False,blank=False)
    phone_number = models.CharField(max_length=10,null=False,blank=False)
    date_modified = models.DateTimeField(auto_now=True)
    date_created =  models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return  self.email

    
# Recruiter job table 
class Recruiter_Job(models.Model):
    cat=models.CharField(max_length=50,null=False,blank=False)
    title=models.CharField(max_length=50,null=False,blank=False)
    description=models.CharField(max_length=50,null=False,blank=False)
    year_of_experience=models.CharField(max_length=50,null=False,blank=False)
    country=models.CharField(max_length=50,null=False,blank=False)
    education_level=models.CharField(max_length=50,null=False,blank=False)
    degree=models.CharField(max_length=50,null=False,blank=False)
    skill_level=models.CharField(max_length=50,null=False,blank=False)
    recruiter = models.ForeignKey(Recruiter,default=None,on_delete=models.DO_NOTHING)
    is_open= models.BooleanField(null=False,default=False)
    number_of_applicants=models.IntegerField(null=False,blank=False,default=0)
    max_number_of_applicants = models.IntegerField(null=False,blank=False,default=1)
    selected_applicants = models.IntegerField(null=False,blank=False,default=0)
    date_modified = models.DateTimeField(auto_now=True)
    date_created =  models.DateTimeField(auto_now_add=True) 


    def __str__(self):
        return self.title

# Candidate Applications Table 
class Candidate_Applications(models.Model):
    year_of_experience=models.CharField(max_length=50,null=False,blank=False)
    country=models.CharField(max_length=50,null=False,blank=False)
    education_level=models.CharField(max_length=50,null=False,blank=False)
    degree=models.CharField(max_length=50,null=False,blank=False)
    skill_level=models.CharField(max_length=50,null=False,blank=False)
    job = models.ForeignKey(Recruiter_Job,default=None, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(Candidate,default=None, on_delete=models.DO_NOTHING)
    is_selected= models.BooleanField(null=False,default=False)
    number_of_applicants=models.IntegerField(null=False,blank=False,default=0)
    selected_applicants = models.IntegerField(null=False,blank=False,default=0)
    date_modified = models.DateTimeField(auto_now=True)
    date_created =  models.DateTimeField(auto_now_add=True) 


    def __str__(self):
        return 'Application For '+self.job.title+' by '+self.candidate.user.username



    
