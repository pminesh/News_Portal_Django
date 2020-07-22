# Generated by Django 3.0.2 on 2020-02-07 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DailyNews', '0002_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newsarticle', models.IntegerField()),
                ('reporters', models.IntegerField()),
                ('awardswon', models.IntegerField()),
                ('yearold', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('positions', models.CharField(choices=[('1', 'Reporter'), ('2', 'Bureau chief / editor'), ('3', 'Section editor'), ('4', 'Copy editor'), ('5', 'News editor'), ('6', 'Company lawyer'), ('7', 'Graphics people'), ('8', 'Stipple portrait artists'), ('9', 'Company lawyer'), ('10', 'Online staff'), ('11', 'Videographer'), ('12', 'Market data group'), ('13', 'Library'), ('14', 'deputy managing editor')], max_length=25)),
                ('image', models.ImageField(blank=True, upload_to='employee_prof')),
            ],
        ),
    ]