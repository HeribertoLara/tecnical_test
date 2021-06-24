# Generated by Django 2.2.14 on 2021-06-24 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
        ('users', '0002_user_adress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='adress',
        ),
        migrations.AddField(
            model_name='user',
            name='adress',
            field=models.ManyToManyField(related_name='users', to='addresses.Address'),
        ),
    ]
