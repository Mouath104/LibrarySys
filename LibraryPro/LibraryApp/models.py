from django.db import models
from django.contrib.auth.models import User 
from datetime import datetime,timedelta
# Create your models here.

class Student(models.Model):
    FName=models.CharField(max_length=10)
    LName=models.CharField(max_length=10)
    TelNo=models.CharField(max_length=10)
    user=models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    # file = models.FileField(upload_to='documents/',default='default.jpg')
    image = models.ImageField(upload_to='static/images/Students/',  blank=True)
    # std_img=models.ImageField(upload_to='images/', default='default.jpg')

    def __str__(self):
        return f'{self.FName} {self.LName}'
        
# < Book related Classes
class Auther(models.Model):
    Name=models.CharField(max_length=15)
    Loc=models.CharField(max_length=15)
    About=models.CharField(max_length=100)

    def __str__(self):
        return self.Name

class Category(models.Model):
    Name=models.CharField(max_length=15)
    
    def __str__(self):
        return self.Name


class Book(models.Model):
    Name=models.CharField(max_length=15)
    Price=models.PositiveIntegerField()
    Desc=models.CharField(max_length=100)
    cat=models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="books"
    )
    auther=models.ForeignKey(
        Auther,
        on_delete=models.CASCADE,
        related_name="books"
    )
    
    def __str__(self):
        return self.Name

# />

def expiry():
    return datetime.today() + timedelta(days=14)

class Issued_Book(models.Model):
    book=models.OneToOneField(
        Book,
        on_delete=models.CASCADE,
    )
    issued_date = models.DateField(auto_now=True)
    expiry_date = models.DateField(default=expiry)
    student=models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="issued_books"
    )
    
    def __str__(self):
        return f'{self.student.FName}-{self.book}'
