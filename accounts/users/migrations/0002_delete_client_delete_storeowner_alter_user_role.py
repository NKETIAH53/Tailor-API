# Generated by Django 4.0.6 on 2022-08-30 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='StoreOwner',
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('SO', 'Owner'), ('CL', 'Client')], max_length=20),
        ),
    ]
