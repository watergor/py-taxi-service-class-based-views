# Generated by Django 4.1 on 2024-12-15 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='driver',
            options={'verbose_name': 'driver', 'verbose_name_plural': 'drivers'},
        ),
        migrations.AlterModelOptions(
            name='manufacturer',
            options={'ordering': ['name']},
        ),
    ]
