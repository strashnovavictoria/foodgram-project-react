from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter

from recipes.models import Ingredient, Recipe


class RecipeFilter(filters.FilterSet):

    is_favorited = filters.BooleanFilter(
        method='get_favorite',
        label='favorite',
    )
    tags = filters.AllValuesMultipleFilter(
        field_name='tags__slug',
        label='tags',
    )
    is_in_shopping_cart = filters.BooleanFilter(
        method='get_is_in_shopping_cart',
        label='shopping_cart',
    )

    class Meta:
        model = Recipe
        fields = (
            'tags',
            'author',
            'is_favorited',
            'is_in_shopping_cart',
        )

    def get_favorite(self, queryset, name, value):
        if value:
            return queryset.filter(in_favorite__user=self.request.user)
        return queryset.exclude(
            in_favorite__user=self.request.user
        )

    def get_is_in_shopping_cart(self, queryset, name, value):
        if value:
            return Recipe.objects.filter(
                shopping_recipe__user=self.request.user
            )


class IngredientSearchFilter(SearchFilter):
    search_param = 'name'
