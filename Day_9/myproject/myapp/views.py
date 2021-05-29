from django.shortcuts import render
from .forms import LibraryForm
from .models import Library
from django.http import HttpResponse

# Create your views here.
def addBook(req):
    form  = LibraryForm()
    if req.method == 'POST': 
        form = LibraryForm(req.POST)
        if form.is_valid():
            print(form.data)
            print(form.cleaned_data)
            name = form.data['book_name']
            number = form.data['book_number']
            author = form.data['author']
            dept = form.data['department']
            date = form.data['Publication_Date']
            obj = Library(Book_Name=name,Book_Number=number,Author=author,Department=dept,Publication_Date=date)
            obj.save()
            return HttpResponse("Book Added!!")
        else:
            return HttpResponse("Invalid")
    return render(req,'books.html', {'form' : form})