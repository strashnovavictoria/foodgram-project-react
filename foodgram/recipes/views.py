import datetime

from django.shortcuts import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from recipes.pagination import LimitPaginaton
from recipes.filters import IngredientSearchFilter, RecipeFilter
from recipes.models import (Ingredient, Recipe, Tag, RecipeIngredient)
from recipes.permissions import IsAdminOrReadOnly, IsAuthorOrAdmin
from recipes.serializers import (
    RecipeAddSerializer,
    IngredientSerializer,
    RecipeSerializer,
    RecipeShowSerializer,
    TagSerializer
)


class TagsViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = None
    permission_classes = (IsAdminOrReadOnly,)


class IngredientsViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    pagination_class = None
    filter_backends = (IngredientSearchFilter,)
    search_fields = ('^name',)


class RecipesViewSet(viewsets.ModelViewSet):

    queryset = Recipe.objects.all()
    serializer_classes = {
        'retrieve': RecipeShowSerializer,
        'list': RecipeShowSerializer,
    }
    default_serializer_class = RecipeAddSerializer
    permission_classes = (IsAuthorOrAdmin,)
    filter_backends = [DjangoFilterBackend]
    filterset_class = RecipeFilter
    pagination_class = LimitPaginaton

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action,
                                           self.default_serializer_class)

    def _favorite_shopping_post_delete(self, related_manager):
        recipe = self.get_object()
        if self.request.method == 'DELETE':
            related_manager.get(recipe_id=recipe.id).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        if related_manager.filter(recipe=recipe).exists():
            raise ValidationError('Рецепт уже в избранном')
        related_manager.create(recipe=recipe)
        serializer = RecipeSerializer(instance=recipe)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True,
            permission_classes=[permissions.IsAuthenticated],
            methods=['POST', 'DELETE'], )
    def favorite(self, request, pk=None):
        return self._favorite_shopping_post_delete(
            request.user.favorite
        )

    @action(detail=True,
            permission_classes=[permissions.IsAuthenticated],
            methods=['POST', 'DELETE'], )
    def shopping_cart(self, request, pk=None):
        return self._favorite_shopping_post_delete(
            request.user.shopping_user
        )


class DownloadShoppingCart(APIView):

    permission_classes = [permissions.IsAuthenticated],

    def get(self, request):
        shopping_list = {}
        ingredients = RecipeIngredient.objects.filter(
            recipe__purchases__user=request.user
        )
        for ingredient in ingredients:
            amount = ingredient.amount
            name = ingredient.ingredient.name
            measurement_unit = ingredient.ingredient.measurement_unit
            if name not in shopping_list:
                shopping_list[name] = {
                    'measurement_unit': measurement_unit,
                    'amount': amount
                }
            else:
                shopping_list[name]['amount'] += amount
        main_list = ([f"* {item}:{value['amount']}"
                      f"{value['measurement_unit']}\n"
                      for item, value in shopping_list.items()])
        today = datetime.date.today()
        main_list.append(f'\n, {today.year}')
        response = HttpResponse(main_list, 'Content-Type: text/plain')
        response['Content-Disposition'] = 'attachment; filename="list.txt"'
        return response
