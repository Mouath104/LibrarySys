from django.shortcuts import render,redirect
from LibraryApp import models
from .forms import AddBooksForm,Issued_BookForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login as auth_login
# Create your views here.
def AddBooks(req):
    form = AddBooksForm(req.POST or None)
    if req.method =="POST":
        if form.is_valid():
            form = AddBooksForm(req.POST) 
            form.save()
            return redirect('LibraryApp:Books')
    else:
        form= AddBooksForm()
        return render(req,'Library/addBooks.html',{'form':form})

def Books(req):
    books=models.Book.objects.all()
    con={
        'books':books
    }
    return render(req,'Library/Books.html',con)

def delBook(req,pk):
    deletedBook=models.Book.objects.get(id=pk)
    deletedBook.delete()
    
    return redirect('LibraryApp:Books')

def Students(req):
    students=models.Student.objects.all()
    con={
        'students':students
    }
    return render(req,'Library/Students.html',con)

def delStudents(req,pk):
    deletedStudent=models.Student.objects.get(id=pk)
    deletedStudent.delete()

    return redirect('LibraryApp:Students')

def IssueABook(req):
    form=Issued_BookForm(req.POST or None)
    if req.method=='POST':
        if form.is_valid():
            form=Issued_BookForm(req.POST)
            form.save()
            return redirect('LibraryApp:Issued_Books')
    else:
        form=Issued_BookForm()
        return render(req,'Library/IssueABook.html',{'form':form})

#Login
def login(req):

    if(req.user.is_authenticated):
        return redirect("LibraryApp:Issued_Books") #any home page

    else:
        form = AuthenticationForm(req, data=req.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                auth_login(req, user)
                # messages.info(req, f"You are now logged in as {username}.")
                return redirect("LibraryApp:Issued_Books") #any home page
            else:
                messages.error(req,"Invalid username or password.")
        # else:
            # messages.error(req,"Invalid username or password.")
        form = AuthenticationForm() # get method
        return render(request=req, template_name="Reg/Login.html", context={"login_form":form})

def Issued_Books(req):
    if(req.user.is_authenticated):
        if req.user.is_superuser:
            IssuedBooks=models.Issued_Book.objects.all() #all the issued Books
        else:
            IssuedBooks=models.Issued_Book.objects.filter(
                student_id=req.user.student.id
            )
        con={
            'IssuedBooks':IssuedBooks
        }
        return render(req,'Library/Issued_Books.html',con)
    else:
        return redirect('LibraryApp:login')
        

