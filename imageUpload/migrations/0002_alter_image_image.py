# Generated by Django 4.1 on 2022-08-17 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageUpload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='image'),
        ),
    ]
