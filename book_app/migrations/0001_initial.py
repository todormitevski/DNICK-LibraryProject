# Generated by Django 5.0.6 on 2024-05-19 16:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('year_founded', models.IntegerField()),
                ('website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='')),
                ('isbn', models.CharField(max_length=20)),
                ('year_published', models.IntegerField()),
                ('num_pages', models.IntegerField()),
                ('dimensions', models.CharField(max_length=20)),
                ('book_type', models.CharField(choices=[('SOF', 'Soft'), ('HAR', 'HARD')], max_length=10)),
                ('book_category', models.CharField(choices=[('ROM', 'Romance'), ('THR', 'Thriller'), ('BIO', 'Biography'), ('CLA', 'Classic'), ('DRA', 'Drama'), ('HIS', 'History')], max_length=20)),
                ('price', models.IntegerField()),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_app.publisher')),
            ],
        ),
    ]
