# Generated by Django 4.2.7 on 2023-12-10 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('n_air', '0003_rename_types_sneakers_type_sneakers_character'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sneakers',
            old_name='types_price',
            new_name='price_type',
        ),
        migrations.AddField(
            model_name='sneakers',
            name='price',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]