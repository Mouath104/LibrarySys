from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from LibraryApp import models
from .forms import AddBooksForm,Issued_BookForm,editProfileForm,AddStudentsForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth import update_session_auth_hash
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

def Profile(req, pk=None):
    if req.user.is_authenticated:
        if pk is None:
            # If no `pk` is provided, use the current user's student ID
            student = req.user.student
        else:
            # Otherwise, use the provided `pk` to retrieve the corresponding student
            student = models.Student.objects.get(id=pk)
        
        con = {
            'student': student
        }
        return render(req, 'Reg/Profile.html', con)
    else:
        msg = 'impossible, need to login!'
        return render(req, 'Reg/ERR.html', {'msg': msg})

def chnagePass(req):
    user=models.User.objects.get(id=req.user.id)
    if req.method=="POST":
        if user.check_password(req.POST['curr-pass']):
            user.set_password(req.POST['new-pass'])
            user.save()
            update_session_auth_hash(req,user) # to keep user logged in after changing the Password
        # if(req.POST['old-pass']==req.user.password):
        #     if(req.POST['new-pass']==req.POST['confirm-new-pass']):
        #         user.password=req.POST['new-pass']
        #         user.save()
        else:
            return HttpResponse('Not Equal') # to be replaced by client-side validations
        return redirect('LibraryApp:Profile')
        
    else:
        return render(req,'Reg/changePass.html',{})

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
        msg='impossible, need to login!'
        return render(req,'Reg/ERR.html',{'msg':msg})
        # return HttpResponse('impossible, need to login!')  # to be replaced by Messsege later  
                  
#### Library

def AddStudents(req):
    if req.user.is_superuser: 
        usernames = models.User.objects.values_list('username', flat=True) # to check uniquness  
        if req.method=='POST':
            form = AddStudentsForm(req.POST,req.FILES)
            if form.is_valid():
                if (not req.POST['username'] in usernames):
                    user=models.User.objects.create(username=req.POST['username'],password=req.POST['password'])
                    stdForm=form.save(commit=False)
                    stdForm.image=req.FILES
                    stdForm.user=user
                    stdForm.save()
                    return redirect('LibraryApp:Students')
                else:
                    return HttpResponse("This username is Already") # to be replaced with a message later
        else:
            form = AddStudentsForm()
            return render(req,'Library/addStudent.html',{'form':form})
    else:
        return HttpResponse('impossible, not Autherized!')  # to be replaced by Messsege later
          
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

# the templates filter is not workign with me somehow, i'm done!
# to check the Expiration
from datetime import datetime

def is_expired(item):
    now = datetime.now().date()
    return item < now

def Issued_Books(req):
    if(req.user.is_authenticated):
        expList=[]
        if req.user.is_superuser:
            IssuedBooks=models.Issued_Book.objects.all() #all the issued Books
            for i in IssuedBooks:
                expList.append(is_expired(i.expiry_date))
        else:
            IssuedBooks=models.Issued_Book.objects.filter(
                student_id=req.user.student.id
            )
            for i in IssuedBooks:
                expList.append(is_expired(i.expiry_date))
        # i tried to make custome filter in templates with no result
        zippedList=zip(IssuedBooks,expList)
        con={
            'IssuedBooks':IssuedBooks,
            'expList':expList,
            'zippedList':zippedList
        }
        return render(req,'Library/Issued_Books.html',con)
    else:
        return redirect('LibraryApp:login')
        
def retract(req,pk):
    if(req.user.is_superuser): 
        retractIssue = models.Issued_Book.objects.get(id=pk)
        retractIssue.delete()
        return redirect('LibraryApp:Issued_Books')
    else:
        return HttpResponse('impossible, not Autherized!')  # to be replaced by Messsege later 


def bookDetails(req,pk):
    if(req.user.is_authenticated):
        book=models.Book.objects.get(id=pk)
        con={
            'book':book
        }
        return render(req,'Library/bookDetails.html',con)
    else:
        return redirect('LibraryApp:login')


#PDF

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from django.http import FileResponse
import io
from reportlab.lib.units import inch

def PDF(req):
    books = models.Book.objects.all()
    buffer = io.BytesIO()

    # Create a PDF document
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []

    # Define column headers and calculate column widths
    columns = ["Name", "Price", "Category", "Author"]
    col_widths = [int(letter[0]*0.15), int(letter[0]*0.1), int(letter[0]*0.15), int(letter[0]*0.2)]

    # Create table data
    data = [columns]
    for b in books:
        data.append([b.Name, str(b.Price), b.cat.Name, b.auther.Name])

    # Create table and add to elements list
    table = Table(data, colWidths=col_widths)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    elements.append(table)

    # Add "Printed by: [user name]" text to the PDF
    user_name = req.user.get_full_name() if req.user.get_full_name() else req.user.username
    styles = getSampleStyleSheet()
    text = f"Printed by: {user_name}"
    text_obj = Paragraph(text, styles["Normal"])
    elements.append(Spacer(1, 0.2*inch))
    elements.append(text_obj)

    # Build PDF document and return response
    doc.build(elements)
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='Books.pdf')
