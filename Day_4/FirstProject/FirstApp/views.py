from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def home(req):
#     return HttpResponse("Welcome APSSDC")

# def about(req):
#     return HttpResponse("Hello!! Everyone. This is Kowshik407")

def welcome(req,myname,id):
    return HttpResponse(" Hello!! A warm welcome to you Mr. " + myname + " and your roll number is " + str(id))

def roll(req,id):
    return HttpResponse("Your roll number is " + str(id)) 
    # Note You cannot print an integer in HTML page. So you can convert into string

def student(req,name,age,email):
    return HttpResponse("The Student name is {} and his age is {} and his email address is {}.".format(name, age, email))
    # Note here int conversion is not be done. But by using format specifiers it becomes easier. Therefore, try to have format specifiers.

def table(req,n):
    # return HttpResponse(["{} * {} = {}".format(n,i,n*i)] for i in range(1,11))
    result = []
    for i in range(1,11):
        result.append("{} x {} = {} ".format(n,i,n*i))
    return HttpResponse(result)

# HTML Pages

def home(req):
    info = {"name": 'Kowshik407', 'age':18}
    return render(req,'home.html', {'data':info})

def about(req):
    return render(req,'about.html')

def aphome(req):
    return render(req,'aphome.html')

def apabout(req):
    return render(req,'apabout.html')