# Generated by Django 3.2.9 on 2022-10-04 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BibliotecaApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='imagem',
            field=models.FileField(default=1, upload_to='media/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]
