# Generated by Django 5.0.7 on 2024-07-29 18:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                    "name",
                    models.CharField(max_length=50, verbose_name="Название категории"),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="Описание категории"
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                    "name",
                    models.CharField(max_length=50, verbose_name="Название продукта"),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="Описание продукта"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="product/photo",
                        verbose_name="Фото продукта",
                    ),
                ),
                ("price", models.FloatField(blank=True, null=True, verbose_name="")),
                (
                    "created_at",
                    models.DateTimeField(blank=True, null=True, verbose_name=""),
                ),
                (
                    "updated_at",
                    models.DateTimeField(blank=True, null=True, verbose_name=""),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="Products",
                        to="catalog.category",
                        verbose_name="",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
                "ordering": ["name", "category", "price"],
            },
        ),
    ]
