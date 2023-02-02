from django import forms
from LibraryApp.models import Book,Issued_Book,User,Student

class AddBooksForm(forms.ModelForm):   
    class Meta:
        model = Book
        exclude = ("", )

class Issued_BookForm(forms.ModelForm):
    class Meta:
        model=Issued_Book
        exclude = ("", )

class editProfileForm(forms.ModelForm):
    class Meta:
        model=Student
        exclude = ("user", )
# class regStudentForm(forms.ModelForm):
#     class Meta:
#         model=User
#         exclude = ("last_login","is_superuser","is_staff", "is_active","date_joined","groups","user_permissions")

# class regAdminForm(forms.ModelForm):
#     class Meta:
#         model=User
#         exclude = ('',)