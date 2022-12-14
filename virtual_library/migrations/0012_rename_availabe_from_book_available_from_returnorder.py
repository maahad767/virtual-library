# Generated by Django 4.1 on 2022-08-21 21:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('virtual_library', '0011_alter_rating_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='availabe_from',
            new_name='available_from',
        ),
        migrations.CreateModel(
            name='ReturnOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('return_date', models.DateField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='virtual_library.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Return Order',
                'verbose_name_plural': 'Return Orders',
            },
        ),
    ]
