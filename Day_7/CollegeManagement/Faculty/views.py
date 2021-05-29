from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(req):
    return render(req, 'Faculty/index.html')

def register(req):
    if req.method == "POST":
        # If you use print function we can have this output in cmd 
        a = req.POST['username']
        b = req.POST['age']
        c = req.POST['email']
        return render(req,'Faculty/showdata.html', {'a' : a, 'b' : b, 'c' : c})
    return render(req, 'Faculty/register.html')

def about(req):
    return render(req, 'Faculty/about.html')

def contact(req):
    return render(req, 'Faculty/contact.html')
