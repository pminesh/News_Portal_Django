# Generated by Django 3.0.2 on 2020-03-04 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DailyNews', '0007_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='userimage',
            field=models.ImageField(upload_to='profile_image'),
        ),
    ]
