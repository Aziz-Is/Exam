from django.db import models

# Create your models here.

class Book(models.Model):
    STATUS_CHOICES = [("active", "Активно"),("blocked", "Заблокировано")]
    author = models.CharField(max_length=200, null=False, blank=False, verbose_name='имя автора записи')
    email = models.EmailField(null=False, blank=False, verbose_name='почта автора записи')
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='текст записи ')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='время редактирования')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, null=False, blank=False, default='active')

    def __str__(self):
        return f'{self.author} {self.status}'

    class Meta:
        db_table = 'book'
