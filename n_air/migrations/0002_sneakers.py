# Generated by Django 4.2.7 on 2023-11-27 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('n_air', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sneakers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('types_price', models.ImageField(choices=[("So'm", "So'm"), ('rubl', 'rubl'), ('Dollr', 'Dollr')], default="So'm", max_length=10, upload_to='')),
                ('images', models.ImageField(upload_to='')),
                ('types', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='n_air.category')),
            ],
        ),
    ]
