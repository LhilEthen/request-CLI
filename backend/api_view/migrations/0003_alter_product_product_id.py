# Generated by Django 4.2.3 on 2023-09-04 12:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api_view', '0002_remove_product_id_product_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
    ]
