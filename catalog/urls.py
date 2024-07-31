from catalog.apps import CatalogConfig
from django.urls import path
from catalog.views import home
from catalog.views import contacts
from catalog.views import product

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name="home"),
    path('contacts/', contacts, name="contacts"),
    path('product/<int:pk>', product, name="product"),

]
