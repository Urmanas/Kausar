
from django.shortcuts import render
from django.db.models import Prefetch

from .models import Category, Product


def menu_list(request):
    active_category = request.GET.get("category", "")

    available_products = Product.objects.filter(
        is_available=True
    )

    categories = (
        Category.objects
        .filter(products__is_available=True)
        .distinct()
        .order_by("sort_order", "name")
    )

    if active_category.isdigit():
        selected_id = int(active_category)

        if categories.filter(pk=selected_id).exists():
            categories = categories.filter(pk=selected_id)
        else:
            active_category = ""
    else:
        active_category = ""

    categories = categories.prefetch_related(
        Prefetch(
            "products",
            queryset=available_products.order_by(
                "sort_order", "name"
            ),
            to_attr="available_products",
        )
    )

    all_categories = (
        Category.objects
        .filter(products__is_available=True)
        .distinct()
        .order_by("sort_order", "name")
    )

    return render(
        request,
        "menu/menu_list.html",
        {
            "categories": categories,
            "all_categories": all_categories,
            "active_category": active_category,
        },
    )
