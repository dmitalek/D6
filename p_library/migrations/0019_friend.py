# Generated by Django 2.2.6 on 2020-07-05 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0018_auto_20200628_2126'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend_name', models.TextField(verbose_name='Имя друга')),
                ('book', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='freiend_book', to='p_library.Book', verbose_name='Издательство')),
            ],
        ),
    ]