from django.contrib import admin
from .models import Jewelry, CatalogOrder, BuilderModel, BuilderOrder

admin.site.register(Jewelry)
admin.site.register(CatalogOrder)
admin.site.register(BuilderModel)
admin.site.register(BuilderOrder)