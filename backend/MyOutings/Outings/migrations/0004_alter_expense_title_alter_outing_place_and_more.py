# Generated by Django 4.1.2 on 2022-11-01 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Outings', '0003_expense_beneficient_expense_sponsor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='title',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='outing',
            name='place',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='outing',
            name='title',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
