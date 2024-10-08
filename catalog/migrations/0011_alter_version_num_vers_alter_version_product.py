# Generated by Django 5.0.7 on 2024-09-09 18:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0010_version"),
    ]

    operations = [
        migrations.AlterField(
            model_name="version",
            name="num_vers",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Номер версии"
            ),
        ),
        migrations.AlterField(
            model_name="version",
            name="product",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="Products",
                to="catalog.product",
                verbose_name="Продукт",
            ),
        ),
    ]
