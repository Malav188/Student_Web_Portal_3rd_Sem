# Generated by Django 5.0.6 on 2024-07-03 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_gtuexam_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub_syllabus',
            name='type',
            field=models.CharField(choices=[('REGULAR', 'Regular'), ('REMEDIAL', 'Remedial')], default='REGULAR', max_length=10),
        ),
    ]