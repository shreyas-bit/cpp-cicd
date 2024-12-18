# Generated by Django 4.2.16 on 2024-11-12 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
