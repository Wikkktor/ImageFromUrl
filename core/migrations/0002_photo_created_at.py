# Generated by Django 4.1.2 on 2022-10-25 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]