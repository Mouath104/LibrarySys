from django import forms
from LibraryApp.models import Book,Issued_Book,User

class AddBooksForm(forms.ModelForm):   
    class Meta:
        model = Book
        exclude = ("user", )

class Issued_BookForm(forms.ModelForm):
    class Meta:
        model=Issued_Book
        exclude = ("user", )

# class regStudentForm(forms.ModelForm):
#     class Meta:
#         model=User
#         exclude = ("last_login","is_superuser","is_staff", "is_active","date_joined","groups","user_permissions")

# class regAdminForm(forms.ModelForm):
#     class Meta:
#         model=User
#         exclude = ('',)