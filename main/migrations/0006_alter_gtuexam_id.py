# Generated by Django 5.0.6 on 2024-07-03 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_sub_syllabus_assigned_sub_faculty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gtuexam',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
