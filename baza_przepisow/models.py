from django.db import models


class MeasurementUnit(models.Model):
    measurement_desc = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.measurement_desc


class MeasurementQuantity(models.Model):
    qty_amount = models.DecimalField(max_digits=5, decimal_places=2)


class Ingredient(models.Model):
    name = models.CharField(max_length=64, unique=True, blank=False, null=False)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True, blank=False, null=False)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True, blank=False, null=False)

    def __str__(self):
        return self.name

    # ingredient.recipe.id

class Recipe(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    tags = models.ManyToManyField(Tag)
    category = models.ManyToManyField(Category)
    preparation_time = models.CharField(max_length=64, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    bake_temp = models.SmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, blank=False, null=False)
    measurement = models.ForeignKey(MeasurementUnit, on_delete=models.CASCADE, null=True)
    measurement_qty = models.ForeignKey(MeasurementQuantity, on_delete=models.CASCADE, null=True)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        unique_together = ('recipe', 'ingredient',)

