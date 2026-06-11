from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Person(models.Model):
    name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.id_number
    

class ChoiceHorse(models.Model):
    horse_name = models.CharField(max_length=100)
    person = models.OneToOneField(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.person.id_number} - {self.horse_name}'

class HorseTour(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    categories = models.ManyToManyField(Category, blank=True)
    views = models.PositiveIntegerField(db_default=0, null=True)


    def __str__(self):
        return self.title
    

class Comment(models.Model):
    tour = models.ForeignKey(HorseTour,on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author
