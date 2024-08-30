import json
import os

from django.core.management import BaseCommand
from catalog.models import Product, Category
from config.settings import BASE_DIR

file_json = os.path.join(BASE_DIR, 'catalog.json')


class Command(BaseCommand):

    @staticmethod
    def load_data():
        """
        Загружает данные из файла json
        """
        try:
            with open(file_json, 'r', encoding='utf-8') as f:
                json_data = json.load(f)
        except Exception as e:
            print("Error: ", e)
        else:
            return json_data

    @staticmethod
    def json_read_categories(data):
        categories_data = []
        for item in data:
            if item["model"] == "catalog.category":
                categories_data.append(item)
        return categories_data

    @staticmethod
    def json_read_products(data):
        products_data = []
        for item in data:
            if item["model"] == "catalog.product":
                products_data.append(item)
        return products_data

    def handle(self, *args, **options):

        # Удалите все продукты
        Category.objects.all().delete()
        # Удалите все категории
        Product.objects.all().delete()

        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

        data_json = self.load_data()

        # Обходим все значения категорий из фикстуры для получения информации об одном объекте
        for category in Command.json_read_categories(data_json):
            category_for_create.append(
                Category(id=category["pk"], name=category["fields"]["name"],
                         description=category["fields"]["description"])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фикстуры для получения информации об одном объекте
        for product in Command.json_read_products(data_json):
            if product["fields"]["category"]:
                category_product = Category.objects.get(pk=product["fields"]["category"])
            else:
                category_product = None
            product_for_create.append(
                Product(id=product["pk"], name=product["fields"]["name"],
                        description=product["fields"]["description"],
                        image=product["fields"]["image"],
                        category=category_product,
                        price=product["fields"]["price"], created_at=product["fields"]["created_at"],
                        updated_at=product["fields"]["updated_at"])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
