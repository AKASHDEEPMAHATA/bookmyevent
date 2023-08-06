# Generated by Django 4.2 on 2023-08-06 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_categories_price_type_alter_event_details_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event_details',
            name='unique_id',
        ),
        migrations.AlterField(
            model_name='event_details',
            name='category',
            field=models.CharField(choices=[('EDUCATIONAL', 'EDUCATIONAL'), ('SPORTS', 'SPORTS'), ('CAREER', 'CARRER'), ('SPIRITUAL', 'SPIRITUAL'), ('COMEDY', 'COMEDY'), ('CULTURAL', 'CULTURAL'), ('OTHERS', 'OTHERS')], max_length=200),
        ),
        migrations.AlterField(
            model_name='event_details',
            name='price_tag',
            field=models.CharField(choices=[('FREE', 'FREE'), ('PAID', 'PAID')], max_length=200),
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
        migrations.DeleteModel(
            name='Price_Type',
        ),
    ]
