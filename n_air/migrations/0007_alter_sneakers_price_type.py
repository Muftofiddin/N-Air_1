# Generated by Django 4.2.7 on 2023-12-10 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('n_air', '0006_alter_sneakers_price_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sneakers',
            name='price_type',
            field=models.ImageField(choices=[("So'm", "So'm"), ('rubl', 'rubl'), ('$', '$')], default="So'm", max_length=10, upload_to=''),
        ),
    ]