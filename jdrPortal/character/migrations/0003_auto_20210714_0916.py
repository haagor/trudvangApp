# Generated by Django 3.2 on 2021-07-14 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0002_alter_character_traits'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='archetypes',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='culture',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='race',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]