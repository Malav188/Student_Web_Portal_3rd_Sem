# Generated by Django 4.2.5 on 2023-09-25 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_syllabus_sub_assigned_faculty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='syllabus',
            name='sub_assigned_faculty',
        ),
    ]