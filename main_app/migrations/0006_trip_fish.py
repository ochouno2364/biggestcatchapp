# Generated by Django 5.2.2 on 2025-06-15 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_fish_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='fish',
            field=models.ManyToManyField(to='main_app.fish'),
        ),
    ]
