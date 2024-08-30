from catalog.apps import CatalogConfig
from django.urls import path
from catalog.views import ProductListView, ProductDetailView, CategoryDetailView, without_category
from catalog.views import ProductCreateView, ProductUpdateView, ProductDeleteView
from catalog.views import BlogRecordListView, BlogRecordDetailView, BlogRecordCreateView
from catalog.views import BlogRecordDeleteView, BlogRecordUpdateView, ContactsCreateView
app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name="product_list"),
    path('contacts/', ContactsCreateView.as_view(), name="contacts"),
    path('category/0', without_category, name="without_category"),
    path('category/<int:pk>', CategoryDetailView.as_view(), name="category"),
    path('product/<int:pk>', ProductDetailView.as_view(), name="product"),
    path('product/create', ProductCreateView.as_view(), name="product_create"),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name="product_update"),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name="product_delete"),
    path('blog/', BlogRecordListView.as_view(), name="blogrecord_list"),
    path('blog/<int:pk>', BlogRecordDetailView.as_view(), name="blogrecord"),
    path('blog/create', BlogRecordCreateView.as_view(), name="blogrecord_create"),
    path('blog/<int:pk>/update/', BlogRecordUpdateView.as_view(), name="blogrecord_update"),
    path('blog/<int:pk>/delete/', BlogRecordDeleteView.as_view(), name="blogrecord_delete"),
]
