# Generated by Django 4.2 on 2023-07-12 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stark', '0005_alter_coursemodel_em'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursemodel',
            name='em',
        ),
    ]
