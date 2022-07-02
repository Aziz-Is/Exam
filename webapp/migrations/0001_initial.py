# Generated by Django 4.0.5 on 2022-07-02 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200, verbose_name='имя автора записи')),
                ('email', models.EmailField(max_length=254, verbose_name='почта автора записи')),
                ('text', models.TextField(max_length=3000, verbose_name='текст записи ')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='время редактирования')),
                ('status', models.CharField(choices=[('active', 'Активно'), ('blocked', 'Заблокировано')], default='active', max_length=50)),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]
