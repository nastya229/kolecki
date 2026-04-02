from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("catalog/", views.catalog, name="catalog"),
    path("about/", views.about, name="about"),
    path("3d-models/", views.models_3d, name="models_3d"),

    # заказ из каталога (сразу отправка в ТГ)
    path("order/<int:id>/", views.create_catalog_order, name="catalog_order"),
]