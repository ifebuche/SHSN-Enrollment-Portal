# Generated by Django 3.0.3 on 2020-03-05 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20200305_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_no',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
