from django.urls import path
from LibraryApp import views
app_name = "LibraryApp"

urlpatterns = [
    path('AddBooks/', views.AddBooks,name='AddBooks'),
    path('Books/', views.Books, name='Books'),
    path('delBook/<int:pk>/', views.delBook, name='delBook'),
    path('students/', views.Students, name='Students'),
    path('delStudents/<int:pk>/', views.delStudents, name='delStudents'),
    path('IssueABook/', views.IssueABook, name='IssueABook'),
    path('Issued_Books/', views.Issued_Books, name='Issued_Books'),
    path('', views.login , name='login')
]
