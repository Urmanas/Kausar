from django.contrib import admin

from django.utils.html import format_html 

from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "sort_order",
    )

    list_editable = ("sort_order",)
    search_fields = ("name",)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "image_preview",
        "name",
        "category",
        "price",
        "is_available",
        "sort_order",

    )

    list_display_links = ("name",)

    list_editable = (
        "price",
        "is_available",
        "sort_order",
    )

    list_filter = (
        "category",
        "is_available",
    )

    search_fields = (
        "name", 
        "description",
    )

    list_select_related = ("category",)
    list_per_page = 20

    readonly_fields = (
        "image_preview",
        "created_at",
    )

    fieldsets = (
        ("Product information", {
            "fields": (
                "category",
                "name",
                "description",
                "price"
            )
        }),
        ("Photo", {
            "fields": (
                "image",
                "image_preview",
            )
        }),
        ("Availability", {
            "fields": (
                "is_available",
                "sort_order",
            )
        }),
        ("Other information", {
            "fields": ("created_at",)
        })
    )

    @admin.display(description="Photo")
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" '
                'height="60" style="object-fit:cover; '
                'border-radius:8px;" />',
                obj.image.url,
            )

        return "No photo"

admin.site.site_header = "KAUSAR Administration"
admin.site.site_title = "KAUSAR Admin"
admin.site.index_title = "Coffee & Bakery Management"