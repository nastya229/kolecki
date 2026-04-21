from django.db import models
import os
import uuid
from cloudinary.models import CloudinaryField


def upload_to(instance, filename):
    ext = os.path.splitext(filename)[1]
    return f'jewelry/{uuid.uuid4().hex}{ext}'

class Jewelry(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    image = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.name
    
    @property
    def image_url(self):
        try:
            if self.image and hasattr(self.image, "url"):
                return self.image.url
        except Exception:
            return None
        return None


class CatalogOrder(models.Model):
    jewelry = models.ForeignKey(Jewelry, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Каталог заказ #{self.id}"


class BuilderModel(models.Model):
    PRODUCT_TYPES = [
        ("ring", "Кольцо"),
        ("bracelet", "Браслет"),
        ("earrings", "Серьги"),
    ]

    title = models.CharField(max_length=120)
    product_type = models.CharField(max_length=20, choices=PRODUCT_TYPES)
    glb_file = models.FileField(upload_to="builder_models/", blank=True, null=True)
    allow_engraving = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.get_product_type_display()} — {self.title}"


class BuilderOrder(models.Model):
    PRODUCT_TYPES = [
        ("ring", "Кольцо"),
        ("bracelet", "Браслет"),
        ("earrings", "Серьги"),
    ]

    product_type = models.CharField(max_length=20, choices=PRODUCT_TYPES)
    model = models.ForeignKey(BuilderModel, on_delete=models.SET_NULL, null=True, blank=True)
    material = models.CharField(max_length=50)
    stone = models.CharField(max_length=50, blank=True)
    engraving = models.CharField(max_length=120, blank=True)
    customer_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"3D заказ #{self.id}"