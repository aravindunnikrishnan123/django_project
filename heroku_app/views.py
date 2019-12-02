from django.shortcuts import render
from django.http import HttpResponse
from . models import *
# Create your views here.

def fn_myIndex(request):
    context = {"msg":'initial load'}
    return render(request, 'index.html',context)

def fn_userLogin(request):
    if request.method == 'POST':
        try:
            login_obj = Login.objects.get(username=username)
            if login_obj.password == password:
                return render(request,'index.html')
            return HttpResponse('incorrect password')
        except Exception as e:
            return HttpResponse('incorrect username')       
    return render(request,'login.html')

def fn_saveUser(request):
    if request.method == 'POST':
        try:
            uname    = request.POST['uname']

            login_exist  = Login.objects.filter(username=uname).exists()

            if login_exist == False:
                fname    = request.POST['fname']
                lname    = request.POST['lname']
                password = request.POST['pass']
                dob      = request.POST['dob']
                gender   = request.POST['gender']
                
                login_obj = Login(username=uname,password=password)
                login_obj.save()

                if login_obj.id > 0:
                    user_obj = UserDetails(first_name=fname,last_name=lname,gender=gender,
                                dob=dob,fk_login=login_obj)
                    user_obj.save()
                if user_obj.id > 0:
                    return HttpResponse('User Registered successfully')
            else:
                return HttpResponse('Username already exist')
        except Exception as e:
            return HttpResponse('invalid')    
    return render(request,'register.html')