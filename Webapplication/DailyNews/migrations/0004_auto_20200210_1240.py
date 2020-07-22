# Generated by Django 3.0.2 on 2020-02-10 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DailyNews', '0003_about_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='positions',
            field=models.CharField(choices=[('Reporter', 'Reporter'), ('Bureau chief / editor', 'Bureau chief / editor'), ('Section editor', 'Section editor'), ('Copy editor', 'Copy editor'), ('News editor', 'News editor'), ('Company lawyer', 'Company lawyer'), ('Graphics people', 'Graphics people'), ('Stipple portrait artists', 'Stipple portrait artists'), ('Company lawyer', 'Company lawyer'), ('Online staff', 'Online staff'), ('Videographer', 'Videographer'), ('Market data group', 'Market data group'), ('Library', 'Library'), ('Deputy managing editor', 'Deputy managing editor')], max_length=25),
        ),
    ]