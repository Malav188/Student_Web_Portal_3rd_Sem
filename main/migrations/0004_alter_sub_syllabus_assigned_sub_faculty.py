# Generated by Django 5.0.6 on 2024-07-01 16:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_sub_syllabus_sub_pdf'),
        ('user', '0004_alter_user_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_syllabus',
            name='Assigned_Sub_Faculty',
            field=models.ForeignKey(default=11, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.faculty'),
        ),
    ]