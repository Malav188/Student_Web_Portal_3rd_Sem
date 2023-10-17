# Generated by Django 4.2.5 on 2023-09-25 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0002_faculty_records_delete_hello'),
        ('home', '0006_delete_student_alter_syllabus_sub_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='syllabus',
            name='sub_assigned_faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty.faculty_records'),
        ),
    ]