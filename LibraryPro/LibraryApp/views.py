from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from LibraryApp import models
from .forms import AddBooksForm,Issued_BookForm,editProfileForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout

# Create your views here.

#home Page
def home(req):
    return render(req,'Library/home.html',{})

def user_logout(request):
    if(request.user.is_authenticated):
        logout(request)
        return redirect("LibraryApp:home")
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
                return redirect("LibraryApp:home")
            else:
                messages.error(req,"Invalid username or password.")
        # else:
            # messages.error(req,"Invalid username or password.")
        form = AuthenticationForm() # get method
        return render(request=req, template_name="Reg/Login.html", context={"login_form":form})

def Profile(req):
    if(req.user.is_authenticated): #in case if the user tried to put the URL manually :d
        student=models.Student.objects.get(id=req.user.student.id)
        con={
            'student':student
        }
        return render(req,'Reg/Profile.html',con)
    else:
        return HttpResponse('impossible, need to login!')  # to be replaced by Messsege later

def chnagePass(req):
    pass

def editProfile(req):
    if(req.user.is_authenticated): #in case if the user tried to put the URL manually :d
        try:
            std = req.user.student
        except Students.DoesNotExist:
            std = Students(user=req.user)
        if req.method=='POST':
            form = editProfileForm(req.POST, instance=std)
            if form.is_valid():
                form.save()
                return redirect('LibraryApp:Profile')
        else:
            form = editProfileForm(instance=std)
            return render(req,'Reg/editProfile.html',{'form':form})
    else:
        return HttpResponse('impossible, need to login!')  # to be replaced by Messsege later  
                  
#### Library

def AddBooks(req):
    if req.user.is_superuser:    
        form = AddBooksForm(req.POST or None)
        if req.method =="POST":
            if form.is_valid():
                form.save()
                return redirect('LibraryApp:Books')
        return render(req,'Library/addBooks.html',{'form':form})
    else:
        return HttpResponse('impossible, not Autherized!')  # to be replaced by Messsege later  

def Books(req):
    if(req.user.is_superuser):    
        books=models.Book.objects.all()
        con={
            'books':books
        }
        return render(req,'Library/Books.html',con)
    else:
        return HttpResponse('impossible, not Autherized!')  # to be replaced by Messsege later  


def delBook(req,pk):
    if(req.user.is_superuser): 
        deletedBook=models.Book.objects.get(id=pk)
        deletedBook.delete()
        return redirect('LibraryApp:Books')
    else:
        return HttpResponse('impossible, not Autherized!')  # to be replaced by Messsege later 

def Students(req):
    if(req.user.is_superuser): 
        students=models.Student.objects.all()
        con={
            'students':students
        }
        return render(req,'Library/Students.html',con)
    else:
        return HttpResponse('impossible, not Autherized!')  # to be replaced by Messsege later 

def delStudents(req,pk):
    if(req.user.is_superuser): 
        deletedStudent=models.Student.objects.get(id=pk)
        deletedStudent.delete()

        return redirect('LibraryApp:Students')
    else:
        return HttpResponse('impossible, not Autherized!')  # to be replaced by Messsege later 


def IssueABook(req):
    if(req.user.is_superuser): 
        form=Issued_BookForm(req.POST or None)
        if req.method=='POST':
            if form.is_valid():
                form.save()
                return redirect('LibraryApp:Issued_Books')
        else:
            return render(req,'Library/IssueABook.html',{'form':form})
    else:
        return HttpResponse('impossible, not Autherized!')  # to be replaced by Messsege later 

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
        

