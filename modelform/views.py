from django.shortcuts import render,redirect
from modelform.form import RegisterForm
from modelform.models import Data
from django.contrib import messages

def home(request): 
    myform = RegisterForm()                                 # here 'myform' is an object call 'RegisterForm' class
    mydata = Data.objects.all()
    if mydata !='':
        return render(request,"index.html",{'form':myform, 'datas':mydata})
    else:
        return render(request,"index.html",{'form':myform})
         

def addData(request):
    if request.method == 'POST': 
        myform = RegisterForm(request.POST)
        if myform.is_valid():
            myform.save()
            messages.success(request,"Record Added Successfully")
            return redirect('home')

def updateData(request,id):
    mydata=Data.objects.get(id=id)
    myform=RegisterForm(instance=mydata)
    if request.method == 'POST':
        myform=RegisterForm(request.POST,instance=mydata)
        if myform.is_valid():
            myform.save()
            messages.success(request,"Record Updated Successfully...!!")
            return redirect('Home')
    context={'forms':myform}
    return render(request,"update.html",context)
# Create your views here.
