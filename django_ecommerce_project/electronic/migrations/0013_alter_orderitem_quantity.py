# Generated by Django 4.2.16 on 2024-11-14 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronic', '0012_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
