# Generated by Django 4.1.2 on 2022-11-09 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0002_alter_profile_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(blank=True, to='Profiles.profile'),
        ),
    ]
