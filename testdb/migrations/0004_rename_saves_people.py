# Generated by Django 4.2.9 on 2024-01-25 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testdb', '0003_rename_people_saves'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Saves',
            new_name='People',
        ),
    ]
