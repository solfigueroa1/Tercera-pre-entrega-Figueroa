# Generated by Django 4.2.3 on 2023-07-15 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='infoextra',
            name='biografia',
            field=models.TextField(null=True),
        ),
    ]