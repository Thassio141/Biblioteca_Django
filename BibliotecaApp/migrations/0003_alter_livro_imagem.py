# Generated by Django 3.2.9 on 2022-10-04 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BibliotecaApp', '0002_livro_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='imagem',
            field=models.ImageField(upload_to='media/%Y/%m/%d/'),
        ),
    ]
