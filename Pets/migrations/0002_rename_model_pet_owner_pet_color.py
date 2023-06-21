# Generated by Django 4.2 on 2023-06-21 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='Model',
            new_name='owner',
        ),
        migrations.AddField(
            model_name='pet',
            name='color',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]