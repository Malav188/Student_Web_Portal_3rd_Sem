# Generated by Django 4.2.5 on 2023-09-25 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0002_faculty_records_delete_hello'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty_records',
            name='id',
        ),
        migrations.AlterField(
            model_name='faculty_records',
            name='fac_id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]