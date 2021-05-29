from django.shortcuts import render
from EmailSend import settings
from django.core.mail import send_mail
from django.http import HttpResponse
import random
from .models import Email
from .forms import EmailForm
from django.core.mail import EmailMessage

# Create your views here.

def message(req):
    if req.method == 'POST':
        tomail = req.POST['email']
        sub = req.POST['subject']
        msg = req.POST['message']
        sender = settings.EMAIL_HOST_USER
        receiver = tomail
        send_mail(sub, msg, sender, [receiver])
        return HttpResponse('<h1>Email Send Successfully </h1>')

    return render(req, 'message.html')

def register(req):
    
    # if req.method == 'POST':
    #     fname = req.POST['firstname']
    #     lname = req.POST['lastname']
    #     email = req.POST['email']
    #     uname = req.POST['username']
    #     password = fname[:2] + str(random.randint(10000,99999)) + lname[:2]
    #     Email.objects.create(firstname = fname, lastname = lname, Email = email, username = uname, password = password)
    #     sub = 'Regarding to your login details'
    #     body = """Hello {} \n\n This is Your Username : {} \n\n Your Password : {} \n\n """.format(uname, uname, password)
    #     sender = settings.EMAIL_HOST_USER
    #     receiver = email
    #     send_mail(sub, body, sender, [receiver]) 
    #     return HttpResponse("<h1> Please Check Your Email Id for Login Details </h1>")

    form = EmailForm(req.POST,req.FILES)

    if form.is_valid():
        username=req.POST['username']
        password=str(random.randint(10000,99999))
        receiver=req.POST['Email']
        sender=settings.EMAIL_HOST_USER
        sub='Regarding to your login details....'
        body = """Hello {} \n\n This is Your Username : {} \n\n Your Password : {} \n\n """.format(username, username, password)
        email = EmailMessage(sub, body, sender, [receiver]) 
        email.content_subtype='html'
        file=req.FILES['img']
        email.attach(file.name,file.read(),file.content_type)
        email.send()
        form.save()
        return HttpResponse('Done')

    form = EmailForm()
    return render(req, 'sendmail.html', {'form' : form})