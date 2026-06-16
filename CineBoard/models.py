from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator



# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='movies/')
    language = models.CharField(max_length=100, null=True)
    genres = models.ManyToManyField(Genre, related_name='movies')
    release_date = models.DateField()
    country = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    mark = models.PositiveIntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(10)
    ])
    actors = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} - {self.movie}'
    
class Vip(models.Model):
    seat_num = models.PositiveIntegerField(unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='VIP')
    reserved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.seat_num)