# Generated by Django 4.1 on 2022-08-21 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virtual_library', '0010_rename_stars_rating_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]