from django.urls import path
from LibraryApp import views
app_name = "LibraryApp"

urlpatterns = [
    #REG
    path('',views.home,name='home'), # Home Page
    path('logout/',views.user_logout, name='logout'),
    path('login/', views.login , name='login'),
    path('Profile/', views.Profile, name='Profile'),
    path('editProfile/', views.editProfile,name='editProfile'),
    path('chnagePass/', views.chnagePass,name='chnagePass'),
    #Library
    path('AddStudents/', views.AddStudents, name='AddStudents'),
    path('AddBooks/', views.AddBooks,name='AddBooks'),
    path('Books/', views.Books, name='Books'),
    path('delBook/<int:pk>/', views.delBook, name='delBook'),
    path('students/', views.Students, name='Students'),
    path('delStudents/<int:pk>/', views.delStudents, name='delStudents'),
    path('IssueABook/', views.IssueABook, name='IssueABook'),
    path('Issued_Books/', views.Issued_Books, name='Issued_Books'), 

]
