from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe, RecipeIngredient, MeasurementUnit, MeasurementQuantity, Ingredient
from .forms import RecipeForm, MeasurementUnitForm, MeasurementQuantityForm, IngredientForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.db.models import Q

class SearchResultsView(ListView):
    model = Recipe
    template_name = 'search_results.html'

    def get_queryset(self, request):
        query = request.GET.get("q")
        object_list = Recipe.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query) | Q(tags__name__icontains=query) | Q(category__name__icontains=query)
        )
        return object_list

def filtered_recipies(request):
    srv = SearchResultsView()
    recipies = srv.get_queryset(request)
    ingredients = RecipeIngredient.objects.all()
    return render(request, 'all_recipies.html', {'recipies': recipies, 'ingredients': ingredients, 'filtered': True})



def all_recipies(request):
    recipies = Recipe.objects.all()
    ingredients = RecipeIngredient.objects.all()
    return render(request, 'all_recipies.html', {'recipies': recipies, 'ingredients': ingredients, 'filtered': False})


def all_ingredients(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'all_ingredients.html', {'ingredients': ingredients})


def new_ingredient(request, id):
    # recipe_id = get_object_or_404(Recipe, pk=3)
    # form = RecipeIngredientForm(request.POST or None)
    form_ingredients = IngredientForm(request.POST or None)
    form_qty = MeasurementQuantityForm(request.POST or None)
    # form_qty.fields['qty_amount'].required = False
    form_unit = MeasurementUnitForm(request.POST or None)
    # form_unit.fields['measurement_desc'].required = False

    if request.method == 'POST':
        if form_ingredients.is_valid():
            ingredient =Ingredient.objects.create(**form_ingredients.cleaned_data)
        else:
            ingredient = get_object_or_404(Ingredient, name=form_ingredients.instance.name)

        if form_qty.is_valid():
            qty = MeasurementQuantity.objects.create(qty_amount=form_qty.instance.qty_amount)
        else:
            qty =get_object_or_404(MeasurementQuantity, qty_amount=form_qty.instance.qty_amount)

        if form_unit.is_valid():
            unit = MeasurementUnit.objects.get_or_create(
                measurement_desc=form_unit.instance.measurement_desc.casefold())
        else:
            unit = get_object_or_404(MeasurementUnit, measurement_desc=form_unit.instance.measurement_desc)
        try:
            RecipeIngredient.objects.get_or_create(recipe_id=id, ingredient_id=ingredient.id, measurement_qty_id=qty.id, measurement_id=unit.id)
        except:
            pass

        return redirect(all_recipies)

    return render(request, 'new_ingredient.html', {'form_ingredients': form_ingredients,
                                               'form_qty': form_qty, 'form_unit': form_unit, 'new': True})

@login_required
def new_recipe(request):
    form_recipe = RecipeForm(request.POST or None)

    if form_recipe.is_valid():
        recipe = form_recipe.save()
        obj, created = Recipe.objects.get_or_create(
            name=recipe.name.title(),
            preparation_time=recipe.preparation_time or None,
            description=recipe.description,
            bake_temp=recipe.bake_temp or None,
        )

        return redirect(all_recipies)

    return render(request, 'new_recipe.html', {'form_recipe': form_recipe, 'new': True})
