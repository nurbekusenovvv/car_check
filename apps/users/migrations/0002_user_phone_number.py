# Generated by Django 4.1.7 on 2023-04-10 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default=1, max_length=100, verbose_name='Телефонный номер'),
            preserve_default=False,
        ),
    ]
