from django.shortcuts import render, redirect
from . models import adminsdb,addpreregdb,addvisitorsdb,addrolesdb,usersignupdb
from . forms import addpreregForm,addvisitorsForm,addrolesForm,addadminForm,usersignupForm
from django.contrib.auth.models import auth
from django.contrib import messages
import easygui

def login(request):
    return render(request,'login.html')

def adminlogin(request):
    return render(request,'adminlogin.html')

def userlogin(request):
    if request.method == "POST":  
        form = userloginForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                easygui.msgbox("your data has been saved successfully")
                return redirect('/userhome/')  
            except:  
                pass 
    else:  
        form = userloginForm()  

    return render(request,'userlogin.html',{'form':form})

def usersignup(request):
    if request.method == "POST":  
        form = usersignupForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                easygui.msgbox("your data has been saved successfully")
                return redirect('/userhome/')  
            except:  
                pass 
    else:  
        form = usersignupForm()  

    return render(request,'usersignup.html',{'form':form})
 
def dashboard(request):
    return render(request,'dashboard.html')

def profile(request):
    return render(request,'profile.html')

def department(request):
    return render(request,'department.html')

def designation(request):
    return render(request,'designation.html')

def navemployee(request):
    return render(request,'navemployee.html')

def addprereg(request):
    if request.method == "POST":  
        form = addpreregForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                easygui.msgbox("your data has been saved successfully")
                return redirect('/addprereg/')  
            except:  
                pass 
    else:  
        form = addpreregForm()  

    return render(request,'addprereg.html',{'form':form})


def addadmin(request):
    if request.method == "POST":  
        form = addadminForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                easygui.msgbox("your data has been saved successfully")
                return redirect('/addadmin/')  
            except:  
                pass 
    else:  
        form = addadminForm()  

    return render(request,'addadmin.html',{'none':form})
    

def addvisitors(request):
    if request.method == "POST":  
        form = addvisitorsForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                easygui.msgbox("your data has been saved successfully")
                return redirect('/addvisitors/')  
            except:  
                pass 
    else:  
        form = addvisitorsForm()  

    return render(request,'addvisitors.html',{'form':form})


def addrole(request):
    if request.method == "POST":  
        form = addrolesForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                easygui.msgbox("your data has been saved successfully")
                return redirect('/addrole/')  
            except:  
                pass 
    else:  
        form = addrolesForm()  
    
    return render(request,'addrole.html',{'form':form})


def editvisitors(request):
    return render(request,'editvisitors.html')

def editadmin(request):
    return render(request,'editadmin.html')

def editprereg(request):
    return render(request,'editprereg.html')


def visitors(request):
    employeesvisitors=addvisitorsdb.objects.all()
    return render(request,'visitors.html',{'employeesvisitors':employeesvisitors})

def prereg(request):
    employees=addpreregdb.objects.all()
    return render(request,'prereg.html',{'employees':employees})

def admins(request):
    employeesadmins=adminsdb.objects.all()
    return render(request,'admins.html',{'employeesadmins':employeesadmins})

def roles(request):
    employeesroles=addrolesdb.objects.all()
    return render(request,'roles.html',{'employeesroles':employeesroles})

def editrole(request):
    return render(request,'editrole.html')


def settings(request):
    return render(request,'settings.html')


def userhome(request):
    return render(request,'userhome.html')

def userprereg(request):
    return render(request,'userprereg.html')
