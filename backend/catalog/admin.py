from django.contrib import admin
from . import models
from django.db.models import Count

# Register your models here.


class VariantFilter(admin.SimpleListFilter):
    title = "Variants"
    parameter_name = "variants"

    def lookups(self, request, model_admin):
        return [
            ("yes", "Has Variants"),
            ("no", "No Variants"),
        ]

    def queryset(self, request, queryset):

        if self.value() == "yes":
            return queryset.filter(variant_count__gt=0)

        elif self.value() == "no":
            return queryset.filter(variant_count=0)

        return queryset


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "number_of_variants"]
    list_filter = [VariantFilter]

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(variant_count=Count("variants"))

    def number_of_variants(self, obj):

        return obj.variant_count


admin.site.register(models.ProductVariant)
admin.site.register(models.Category)
admin.site.register(models.Product, ProductAdmin)
