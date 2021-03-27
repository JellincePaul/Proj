from django import forms  
from . models import addpreregdb,addvisitorsdb,addrolesdb,adminsdb,usersignupdb 
class addpreregForm(forms.ModelForm):  
    class Meta:  
        model = addpreregdb
        fields = ['firstname', 'lastname', 'email', 'phone', 'gender', 'emp', 'date', 'time', 'comment', 'address'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = { 'firstname': forms.TextInput(attrs={ 'class': 'form-control' }), 

            'lastname': forms.TextInput(attrs={ 'class': 'form-control' }),

            'email': forms.TextInput(attrs={ 'class': 'form-control' }),
            
            'phone': forms.TextInput(attrs={ 'class': 'form-control' }),

            'gender': forms.TextInput(attrs={ 'class': 'form-control' }),

            'emp': forms.TextInput(attrs={ 'class': 'form-control' }),

            'date': forms.TextInput(attrs={ 'class': 'form-control' }),

            'time': forms.TextInput(attrs={ 'class': 'form-control' }),

            'comment': forms.TextInput(attrs={ 'class': 'form-control' }),

            'address': forms.TextInput(attrs={ 'class': 'form-control' }),
      }



class addvisitorsForm(forms.ModelForm):  
    class Meta:  
        model = addvisitorsdb
        fields = ['firstname', 'lastname', 'email', 'phone', 'gender', 'companyname', 'idnumber', 'emp', 'purpose', 'address'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = { 'firstname': forms.TextInput(attrs={ 'class': 'form-control' }), 

            'lastname': forms.TextInput(attrs={ 'class': 'form-control' }),

            'email': forms.TextInput(attrs={ 'class': 'form-control' }),
            
            'phone': forms.TextInput(attrs={ 'class': 'form-control' }),

            'gender': forms.TextInput(attrs={ 'class': 'form-control' }),

            'companyname': forms.TextInput(attrs={ 'class': 'form-control' }),

            'idnumber': forms.TextInput(attrs={ 'class': 'form-control' }),

            'emp': forms.TextInput(attrs={ 'class': 'form-control' }),

            'purpose': forms.TextInput(attrs={ 'class': 'form-control' }),

            'address': forms.TextInput(attrs={ 'class': 'form-control' }),
      }      



class addrolesForm(forms.ModelForm):  
    class Meta:  
        model = addrolesdb
        fields = ['name'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = { 'name': forms.TextInput(attrs={ 'class': 'form-control' }), 
      }      



class addadminForm(forms.ModelForm):  
    class Meta:  
        model = adminsdb
        fields = ['firstname', 'lastname', 'email', 'phone', 'username', 'password', 'address'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = { 'firstname': forms.TextInput(attrs={ 'class': 'form-control' }), 

            'lastname': forms.TextInput(attrs={ 'class': 'form-control' }),

            'email': forms.TextInput(attrs={ 'class': 'form-control' }),
            
            'phone': forms.TextInput(attrs={ 'class': 'form-control' }),

            'username': forms.TextInput(attrs={ 'class': 'form-control' }),

            'password': forms.TextInput(attrs={ 'class': 'form-control' }),

            'address': forms.TextInput(attrs={ 'class': 'form-control' }),
      }

class usersignupForm(forms.ModelForm):  
    class Meta:  
        model = usersignupdb
        fields = ['name', 'email', 'username', 'password',] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = { 'name': forms.TextInput(attrs={ 'class': 'form-control' }),
        
            'email': forms.TextInput(attrs={ 'class': 'form-control' }),

            'username': forms.TextInput(attrs={ 'class': 'form-control' }),

            'password': forms.TextInput(attrs={ 'class': 'form-control' }),
      }