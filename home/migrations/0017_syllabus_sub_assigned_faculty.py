# Generated by Django 4.2.5 on 2023-09-25 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0004_alter_faculty_records_fac_id'),
        ('home', '0016_remove_syllabus_sub_assigned_faculty'),
    ]

    operations = [
        migrations.AddField(
            model_name='syllabus',
            name='sub_assigned_faculty',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.CASCADE, to='faculty.faculty_records'),
        ),
    ]