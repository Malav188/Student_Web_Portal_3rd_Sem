# Generated by Django 5.0.6 on 2024-07-01 16:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0001_initial'),
        ('main', '0004_alter_sub_syllabus_assigned_sub_faculty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_syllabus',
            name='Assigned_Sub_Faculty',
            field=models.ForeignKey(default=11, null=True, on_delete=django.db.models.deletion.SET_NULL, to='faculty.faculty_records'),
        ),
    ]