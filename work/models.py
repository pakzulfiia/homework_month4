from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CustomUser(User):
    photo = models.ImageField(upload_to='users/')
    phone_number = models.CharField(max_length=15)
    adress = models.CharField(max_length=200, default='Bishkek')
    gender = models.CharField(max_length=100, default='m')
    status = models.CharField(max_length=100, default='married')
    kids = models.CharField(max_length=100, default='none')
    position = models.CharField(max_length=100)
    salary = models.IntegerField(verbose_name='Ожидаемая зарплата?')
    language = models.CharField(max_length=100, default='ru')
    hire_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.username