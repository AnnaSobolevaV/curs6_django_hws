# Generated by Django 5.0.7 on 2024-09-09 18:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0009_blogrecord_updated_at"),
    ]

    operations = [
        migrations.CreateModel(
            name="Version",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "num_vers",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="номер версии"
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=150, verbose_name="Название версии"),
                ),
                (
                    "is_current_vers",
                    models.BooleanField(
                        blank=True, null=True, verbose_name="Текущая версия"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="Products",
                        to="catalog.product",
                        verbose_name="версия",
                    ),
                ),
            ],
            options={
                "verbose_name": "Версия",
                "verbose_name_plural": "Версии",
                "ordering": ("name", "product", "is_current_vers"),
            },
        ),
    ]
