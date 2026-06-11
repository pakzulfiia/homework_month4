from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=100, verbose_name='Укажите название книги')
    author = models.CharField(max_length=100, verbose_name='Укажите автора')
    publication_year = models.IntegerField(verbose_name='Укажите год публикации')
    photo = models.ImageField(upload_to='books_smth/',verbose_name='Загрузите фото книги')
    GENRE = (
        ('Фантастика', 'Фантастика'),
        ('Детектив', 'Детектив'),
        ('Романтика', 'Романтика'),
        ('Проза', 'Проза'),
        ('Драма', 'Драма'),
        ('Психология', 'Психология')
    )
    genre = models.CharField(max_length=100, choices=GENRE, verbose_name='Укажите жанр')
    description = models.TextField(verbose_name='Укажите описание книги')
    PUBLISHER = (
        ('Эксмо', 'Эксмо'),
        ('Издательство АСТ', 'Издательство АСТ'),
        ('РОСМЭН', 'РОСМЭН'),
        ('Азбука-Аттикус', 'Азбука-Аттикус'),
        ('Просвещение', 'Просвещение'),
        ('Image Comics', 'Image Comics')
    )
    publisher = models.CharField(max_length=100, choices=PUBLISHER, verbose_name='укажите издательство')
    pages = models.IntegerField(verbose_name='Укажите количество страниц', blank=True, null=True)
    reserve_book = models.PositiveIntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ], verbose_name='Укажите количество книг для бронирования', default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(db_default=0, null=True)

    class Meta:
        verbose_name = "книга"
        verbose_name_plural = "книги"

    def __str__(self):
        return self.title
