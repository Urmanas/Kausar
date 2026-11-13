from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order", "name"]
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name 


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete = models.PROTECT,
        related_name = 'products'
    )
    name = models.CharField(max_length=150)

    description = models.TextField(
        blank=True
    )

    price = models.DecimalField(
        max_digits = 8,
        decimal_places = 2
    )

    image = models.ImageField(
        upload_to = "products/",
        blank = True, 
        null = True
    )

    is_available = models.BooleanField(
        default = True
    )

    sort_order = models.PositiveIntegerField(
        default = 0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["sort_order", "name"]

    def __str__(self):
        return self.name
