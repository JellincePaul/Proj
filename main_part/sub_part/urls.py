from django.urls import path

from . import views

urlpatterns=[
    path('',views.login,name='login'),
    path('login/',views.login,name='login'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('userlogin/',views.userlogin,name='userlogin'),
    path('usersignup/',views.usersignup,name='usersignup'),
    path('userhome/',views.userhome,name='usehome'),
    path('userprereg/',views.userprereg,name='userprereg'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('profile/',views.profile,name='profile'),
    path('department/',views.department,name='department'),
    path('designation/',views.designation,name='designation'),
    path('navemployee/',views.navemployee,name='navemployee'),
    path('addprereg/',views.addprereg,name='addprereg'),
    path('addadmin/',views.addadmin,name='addadmin'),
    path('addvisitors/',views.addvisitors,name='addvisitors'),
    path('editadmin/',views.editadmin,name='editadmin'),
    path('editprereg/',views.editprereg,name='editprereg'),
    path('editvisitors/',views.editvisitors,name='editvisitors'),
    path('visitors/',views.visitors,name='visitors'),
    path('prereg/',views.prereg,name='prereg'),
    path('admins/',views.admins,name='admins'),
    path('roles/',views.roles,name='roles'),
    path('addrole/',views.addrole,name='addrole'),
    path('editrole/',views.editrole,name='editrole'),
    path('settings/',views.settings,name='settings'),
]