# Generated by Django 4.2.7 on 2023-12-10 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('n_air', '0010_contact_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='phone',
            field=models.IntegerField(default=2, max_length=30),
            preserve_default=False,
        ),
    ]
