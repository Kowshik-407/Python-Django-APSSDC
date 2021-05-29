from django.shortcuts import render
from .forms import MovieForm
from django.http import HttpResponse
from .models import Movies
# Create your views here.
def register(req):
    form=MovieForm(req.POST,req.FILES)
    if form.is_valid():
        form.save()
        return HttpResponse('<h2>Registered Successfully</h2>')
    form=MovieForm()
    return render(req,'register.html',{'form':form})

def login(req):
    if req.method == 'POST':
        mname=req.POST['moviename']
        pwd=req.POST['password']
        data=Movies.objects.all().filter(moviename=mname,password=pwd)
        if data:
            # return HttpResponse('Welcome to User')
            return render(req,'userdetails.html',{'data':data})
        else:
            return HttpResponse('Invalid User')
    return render(req,'login.html')

