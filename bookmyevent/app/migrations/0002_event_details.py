# Generated by Django 4.2 on 2023-08-05 23:27

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('image', models.ImageField(upload_to='Event_images/img')),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('price_tag', models.CharField(choices=[('FREE', 'FREE'), ('PAID', 'PAID')], max_length=200)),
                ('category', models.CharField(choices=[('EDUCATIONAL', 'EDUCATIONAL'), ('SPORTS', 'SPORTS'), ('CAREER', 'CARRER'), ('SPIRITUAL', 'SPIRITUAL'), ('COMEDY', 'COMEDY'), ('CULTURAL', 'CULTURAL'), ('OTHERS', 'OTHERS')], max_length=200)),
                ('location', models.CharField(max_length=500)),
                ('description', ckeditor.fields.RichTextField(null=True)),
                ('timings', ckeditor.fields.RichTextField(null=True)),
                ('main_guest', ckeditor.fields.RichTextField(null=True)),
                ('instruction', ckeditor.fields.RichTextField(null=True)),
            ],
        ),
    ]