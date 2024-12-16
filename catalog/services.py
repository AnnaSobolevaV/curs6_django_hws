from catalog.models import Product, Category


class CategoryService:

    @staticmethod
    def get_product_list(category, request):
        #if category:
        product_list = Product.objects.filter(category=category)
        user = request.user
        if not user.is_authenticated:
            product_list = Product.objects.filter(category=category, is_published=True)
        elif not user.has_perm('catalog.can_unpublish_product'):
            product_list = Product.objects.filter(category=category, is_published=True) | Product.objects.filter(
                category=category, owner=user)
        return product_list

    @staticmethod
    def get_category_list():
        category_list = Category.objects.all()
        return category_list
