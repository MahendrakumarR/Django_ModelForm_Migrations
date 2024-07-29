from django.shortcuts import render
from modelform.form import RegisterForm

def home(request):
    myform = RegisterForm()                                 # here 'myform' is an object call 'RegisterForm' class
    return render(request, 'index.html',{'forms':myform})
# Create your views here.
