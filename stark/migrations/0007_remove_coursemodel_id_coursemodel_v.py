# Generated by Django 4.2 on 2023-07-19 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stark', '0006_remove_coursemodel_em'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursemodel',
            name='id',
        ),
        migrations.AddField(
            model_name='coursemodel',
            name='v',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]