from django.db import models


class Category(models.Model):

    name = models.CharField(
        max_length=50, verbose_name="Название категории", help_text="Название категории"
    )
    description = models.TextField(
        verbose_name="Описание категории", help_text="Описание категории", blank=True, null=True
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=50, verbose_name="Название продукта", help_text="Название продукта"
    )
    description = models.TextField(
        verbose_name="Описание продукта",
        help_text="Описание продукта",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="product/photo/",
        blank=True,
        null=True,
        verbose_name="Фото продукта",
        help_text="Фото продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Категория",
        blank=True,
        null=True,
        related_name="Products",
    )
    price = models.FloatField(
        blank=True, null=True, verbose_name="Цена", help_text="Цена"
    )
    created_at = models.DateTimeField(
        blank=True, null=True, verbose_name="Дата создания", help_text="Дата создания"
    )
    updated_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Дата последнего изменения",
        help_text="Дата последнего изменения",
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = (
            "name",
            "category",
            "price",
        )

    def __str__(self):
        return self.name
