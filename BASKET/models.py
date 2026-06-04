from django.db import models

# Create your models here.
class Thing(models.Model):
    title = models.CharField(max_length=100, verbose_name='укажите название товара')
    photo = models.ImageField(upload_to='buy_things/',verbose_name='загрузите фото товара')
    price = models.IntegerField(verbose_name='укажите цену товара')
    description = models.TextField(verbose_name='укажите описание товара')
    MARK = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    mark = models.CharField(max_length=100, choices=MARK, verbose_name='оцените товар')