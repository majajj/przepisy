from django.contrib import admin
from .models import Ingredient, Recipe, Category, Tag, MeasurementUnit, MeasurementQuantity, RecipeIngredient

admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(RecipeIngredient)
admin.site.register(MeasurementUnit)
admin.site.register(MeasurementQuantity)
