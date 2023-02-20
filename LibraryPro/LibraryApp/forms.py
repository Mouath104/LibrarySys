from django import forms
from LibraryApp.models import Book,Issued_Book,User,Student

# class AddUserForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=("username","password",)

class AddStudentsForm(forms.ModelForm):
    username = forms.CharField(max_length=10, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    class Meta:
        model=Student
        exclude=("user",)

class AddBooksForm(forms.ModelForm):   
    class Meta:
        model = Book
        exclude = ("", )

class Issued_BookForm(forms.ModelForm):
    # we need to excelude the Already Issued Books, as it's one-to-one Rel, as it's impossible for two students to have the same physical Book at same time
    def __init__(self, *args, **kwargs):
        super(Issued_BookForm, self).__init__(*args, **kwargs)
        issued_books_ids = Issued_Book.objects.values_list('book__id', flat=True)
        self.fields['book'].queryset = Book.objects.exclude(id__in=issued_books_ids)

    class Meta:
        model = Issued_Book
        exclude = ("", )

class editProfileForm(forms.ModelForm):
    class Meta:
        model=Student
        exclude = ("user", )

# class chnagePassForm()
# # class regStudentForm(forms.ModelForm):
#     class Meta:
#         model=User
#         exclude = ("last_login","is_superuser","is_staff", "is_active","date_joined","groups","user_permissions")

# class regAdminForm(forms.ModelForm):
#     class Meta:
#         model=User
#         exclude = ('',)