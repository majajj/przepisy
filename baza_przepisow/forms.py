from django import forms
from django.forms import ModelForm
from .models import Recipe, RecipeIngredient, Ingredient, MeasurementUnit, MeasurementQuantity


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'preparation_time', 'description', 'bake_temp']


class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['measurement', 'measurement_qty', 'ingredient', 'recipe']
        unique_together = ['ingredient', 'recipe']


class IngredientForm(ModelForm):

    class Meta:
        model = Ingredient
        fields = ['name']


class MeasurementQuantityForm(ModelForm):
    class Meta:
        model = MeasurementQuantity
        fields = ['qty_amount']


class MeasurementUnitForm(ModelForm):
    class Meta:
        model = MeasurementUnit
        fields = ['measurement_desc']