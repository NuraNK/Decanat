# Generated by Django 3.2.6 on 2022-03-29 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_teachers_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers',
            name='photo',
            field=models.ImageField(upload_to='media/photos/'),
        ),
    ]
