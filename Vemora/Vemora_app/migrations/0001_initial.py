# Generated by Django 5.1 on 2024-09-02 12:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=150)),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_description', models.TextField(max_length=150)),
                ('orgimal_price', models.FloatField()),
                ('selling_price', models.FloatField()),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.TimeField()),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vemora_app.category')),
            ],
        ),
    ]
