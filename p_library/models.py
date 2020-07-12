from django.utils.translation import gettext as _
from django.db import models
  
class Author(models.Model):
    full_name = models.TextField(verbose_name=_("Имя автора"))
    birth_year = models.SmallIntegerField(verbose_name=_("Год рождения"))
    country = models.CharField(max_length=2, verbose_name=_("Страна"))

    def __str__(self):
        return self.full_name

class Maker(models.Model):  
    make_name = models.TextField(default=None, verbose_name=_("Название издательства"))
    make_country = models.CharField(max_length=2, verbose_name=_("Страна издательства"))
      
    def __str__(self):
        return self.make_name

class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField(verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    year_release = models.SmallIntegerField(verbose_name='Год издания')
    copy_count = models.SmallIntegerField(default=0, verbose_name='Кол-во', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Цена', blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор', related_name='book_author')
    publisher = models.ForeignKey(Maker, on_delete=models.SET_DEFAULT, default=1, verbose_name='Издатель')
    friend_name = models.ForeignKey('Friend', on_delete=models.SET_DEFAULT, default=1, verbose_name='Читающий друг')
    avatar = models.ImageField(upload_to='media/%Y/%m/%d ', blank=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f'{self.title} ({self.year_release})'

class BookMaker(models.Model):  
    book = models.ForeignKey('p_library.Book', default=None, on_delete=models.CASCADE, verbose_name=_('Издательство'), related_name='publish_house')
    publisher = models.ForeignKey('p_library.Maker', default=None, on_delete=models.CASCADE, verbose_name=_('Издательство'), related_name='publisher')
    year = models.ForeignKey('p_library.Book', default=None, on_delete=models.CASCADE, verbose_name=_('Год издания'), related_name='publish_year')
    
    class Meta:
        ordering = ['publisher']

    def __str__(self):
        return self.publisher


class Friend(models.Model):
    friend_name = models.TextField(verbose_name=_("Имя друга"))
    friend_book = models.ForeignKey('p_library.Book', on_delete=models.CASCADE, related_name='book', blank=True, verbose_name='Книги')

    class Meta:
        ordering = ['friend_name']

    def __str__(self):
        return self.friend_name
