# Generated by Django 3.1.1 on 2020-10-03 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, verbose_name='Bio'),
        ),
    ]
