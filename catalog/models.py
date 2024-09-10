from django.db import models


class Contacts(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Ваше имя",
        help_text=""
    )
    phone = models.CharField(
        max_length=16,
        verbose_name="Контактный телефон",
        blank=True,
        null=True
    )
    message = models.TextField(
        verbose_name="Сообщение",
        help_text="",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Обращение"
        verbose_name_plural = "Обращения"

    def __str__(self):
        return self.name


class BlogRecord(models.Model):
    header = models.CharField(
        max_length=50,
        verbose_name="Заголовок",
        help_text=""
    )
    slug = models.CharField(
        blank=True,
        null=True,
        max_length=50,
        verbose_name="slug",
        help_text=""
    )
    content = models.TextField(
        verbose_name="Контент",
        help_text="",
        blank=True,
        null=True
    )
    preview = models.ImageField(
        upload_to="blog_record/preview/",
        blank=True,
        null=True,
        verbose_name="",
        help_text="",
    )
    created_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Дата создания",
        help_text=""
    )
    updated_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Дата последнего изменения",
        help_text=""
    )
    is_published = models.BooleanField(
        blank=True,
        null=True,
        verbose_name="Опубликовано",
        help_text=""
    )
    count = models.IntegerField(
        default=0,
        verbose_name="Количество просмотров",
        help_text=""
    )

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

    def __str__(self):
        return self.header


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Название категории",
        help_text=""
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Описание категории",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Название продукта",
        help_text=""
    )
    description = models.TextField(
        verbose_name="Описание продукта",
        help_text="",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="product/photo/",
        blank=True,
        null=True,
        verbose_name="Фото продукта",
        help_text="",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="",
        blank=True,
        null=True,
        related_name="Products",
    )
    price = models.FloatField(
        blank=True,
        null=True,
        verbose_name="Цена",
        help_text=""
    )
    created_at = models.DateTimeField(
        blank=True, null=True,
        verbose_name="Дата создания",
        help_text="Дата создания"
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


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        related_name="Products",
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name="Продукт")
    num_vers = models.PositiveIntegerField(
        verbose_name="Номер версии",
        null=True, blank=True)
    name = models.CharField(
        max_length=150,
        verbose_name="Название версии")
    is_current_vers = models.BooleanField(
        default=False,
        verbose_name="Текущая версия")

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
        ordering = (
            "name",
            "product",
            "is_current_vers",
        )

    def __str__(self):
        return self.name
