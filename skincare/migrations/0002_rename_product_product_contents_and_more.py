# Generated by Django 4.2.16 on 2024-12-09 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skincare', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='product',
            new_name='product_contents',
        ),
        migrations.RenameModel(
            old_name='review',
            new_name='review_contents',
        ),
    ]
