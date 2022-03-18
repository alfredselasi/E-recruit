
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout as auth_logout
from django.core.exceptions import ObjectDoesNotExist
from .models import Recruiter,Candidate,Recruiter_Job,Candidate_Applications

# Create your views here.

#Home/Index View 
def home(request):
    return render(request, 'base/index.html')

# Candidate Login view
def candidateLogin(request):
    if request.method=="POST":
        
       #print(request.POST.get('user_name'))
       user = authenticate(username=request.POST.get('user_name'),password=request.POST.get('password'))
       
       
       if user is not None:
            login(request,user)
            return redirect('/candidate/home')
       else:
            print('auth not working')
            #messages.add_message(request, messages.INFO, 'Invalid Credentials')
            #return redirect('recruiter/login')
    

    return render(request, 'base/candidateLogin.html')


# recruiter login view 
def recruiterLogin(request):
    if request.method=="POST":
        
       #print(request.POST.get('user_name'))
       user = authenticate(username=request.POST.get('user_name'),password=request.POST.get('password'))
       
       
       if user is not None:
            login(request,user)
            return redirect('/recruiter/home')
       else:
            print('auth not working')
            #messages.add_message(request, messages.INFO, 'Invalid Credentials')
            #return redirect('recruiter/login')
    
        

    
    return render (request,'base/recruiterLogin.html')


# candidate home 
def candidateHome(request):
    # get user details
    user_logged_in = request.user

    # get candidate details
    # get candidate applications jobs 
    try:
       get_candidate = Candidate.objects.get(user=user_logged_in)
       # use filter() instead of get() to get (lol) an array
       #applications=Recruiter_Job.objects.filter(recruiter=get_recruiter)
       #print(jobs)

       # get all recruiters 
       jobs = Recruiter_Job.objects.filter()

       
    except ObjectDoesNotExist:
        return redirect('error')

    return render(request,'base/candidateHomePage.html',{'candidate':get_candidate,'jobs':jobs})


#Register Candidate page
def registerCandidate(request):

    if request.method=='POST':
        #create user
        user_candidate = User.objects.create_user(username=request.POST.get('user_name'),password=request.POST.get('password'),email=request.POST.get('email'),first_name=request.POST.get('first_name'),last_name=request.POST.get('last_name'))
        user_candidate.save()
        candidate = Candidate(email=request.POST.get('email'),work_history=request.POST.get('work_history'),user=user_candidate,phone_number=request.POST.get('phone_number'),first_name=request.POST.get('first_name'),last_name=request.POST.get('last_name'))
        candidate.save()
        return redirect('/candidate/login')
    
        
    return render(request,'base/registerCandidate.html')
           


   
    

# Register Recruiter Page 
def registerRecruiter(request):
    if request.method=='POST':
        #create user
        user_recruiter = User.objects.create_user(username=request.POST.get('user_name'),password=request.POST.get('password'),email=request.POST.get('email'),first_name=request.POST.get('first_name'),last_name=request.POST.get('last_name'))
        user_recruiter.save()
        recruiter = Recruiter(email=request.POST.get('email'),company_name=request.POST.get('company_name'),user=user_recruiter,phone_number=request.POST.get('phone_number'),first_name=request.POST.get('first_name'),last_name=request.POST.get('last_name'))
        recruiter.save()
        return redirect('/recruiter/login')
    
    
    
    return render(request,'base/registerRecruiter.html')


    

# Recruiter Home 
def recruiterHome(request):
    # get user details
    user_logged_in = request.user

    # get recruiter details
    # get recruiter jobs 
    try:
       get_recruiter = Recruiter.objects.get(user=user_logged_in)
       # use filter() instead of get() to get (lol) an array
       jobs=Recruiter_Job.objects.filter(recruiter=get_recruiter)
       print(jobs)
       
    except ObjectDoesNotExist:
        return redirect('error')

    return render(request,'base/recruiterHomePage.html',{'user_obj':user_logged_in,'recruiter_obj':get_recruiter,'jobs':jobs})


# Logout 
def logout(request):
    if request.method=="POST":
        auth_logout(request)
        return redirect('/home')



# Post Job @ recruiter home page 
def postJob(request):
    if request.method=="POST":
         # get user details
        user_logged_in = request.user

    # get recruiter details
    try:
       recruiter_obj = Recruiter.objects.get(user=user_logged_in)
       job = Recruiter_Job(cat=request.POST.get('job_cat'),title=request.POST.get('job_title'),max_number_of_applicants=request.POST.get('max_applicants'),description=request.POST.get('desc'),year_of_experience=request.POST.get('exp'),country=request.POST.get('country'),education_level=request.POST.get('education'),degree=request.POST.get('degree'),skill_level=request.POST.get('skill_level'),recruiter=recruiter_obj,is_open=True)
       job.save()
       return redirect('/recruiter/home')
    except ObjectDoesNotExist:
        return redirect('error') 



# view job 
def viewJob(request,job_id):
    # get specific job 
    try:
       job = Recruiter_Job.objects.get(id=job_id)
    except ObjectDoesNotExist:
        return redirect('error') 
    
    return render(request,'base/viewJob.html',{'job':job})


# apply job 
def applyJob(request,job_id):
    if request.method=="POST":
        # Main Logic 
        # Determine if application matches job requirement 
        

        #get job
        try:
            job = Recruiter_Job.objects.get(id=job_id)

            #check if max applicants reached 
            if ((job.number_of_applicants+1) >= job.max_number_of_applicants):
                job.is_open = False
                job.save()
                return redirect('/candidate/home')
            else:
                job.number_of_applicants +=1
                if(request.POST.get('exp')==job.year_of_experience and request.POST.get('country')==job.country and request.POST.get('education')==job.education_level and request.POST.get('degree')==job.degree and request.POST.get('skill_level')==job.skill_level ):
                        # candidate is selected 
                    # update selected in application field in jobs 
                    job.selected_applicants +=1
                    job.save()

                    return redirect('/success')
                else:
                    # Candidate is not selected
                    return redirect('/fail')
                
                
                
            

            

            

            
                

            #print(job.year_of_experience)
        except ObjectDoesNotExist:
            return redirect('error')
        

        


    return render(request,'base/applyJob.html')

# success page 
def successPage (request):
    return render(request,'base/success.html')


# fail page 
def failPage(request):
    return render(request,'base/fail.html')


#error page
def errorPage(request):
    return render(request,'base/404.html')