# Generated by Django 4.2.16 on 2024-11-14 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronic', '0011_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default='delivered', max_length=20),
        ),
    ]
