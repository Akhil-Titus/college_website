# Generated by Django 4.2.4 on 2023-08-07 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credentials_app', '0002_category_product_remove_subject_courses_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='parent_category',
        ),
    ]
