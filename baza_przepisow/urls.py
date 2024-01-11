from django.urls import path
from .views import all_recipies, new_recipe, all_ingredients, new_ingredient, SearchResultsView, filtered_recipies

urlpatterns = [
    path('all/', all_recipies, name='all_recipies'),
    path('all_ingredients/', all_ingredients, name='all_ingredients'),
    path('filtered/', filtered_recipies, name='filtered_recipies'),
    path('new/', new_recipe, name='new_recipe'),
    path('new_ingredient/<int:id>', new_ingredient, name='new_ingredient'),
    path("search/", SearchResultsView.as_view(), name="search_results"),
    ]
