# Generated by Django 2.2.19 on 2022-09-02 13:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import recipes.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteRecipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Избранное',
                'verbose_name_plural': 'Избранные рецепты',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название ингредиента', max_length=200, verbose_name='Название')),
                ('measurement_unit', models.CharField(help_text='Выберите единицу измерения', max_length=50, verbose_name='Единица измерения')),
            ],
            options={
                'verbose_name': 'Ингредиент',
                'verbose_name_plural': 'Ингредиенты',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Укажите название рецепта', max_length=200, unique=True, verbose_name='Название')),
                ('text', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(help_text='Загрузите изображение с фотографией готового блюда', upload_to='recipes/', verbose_name='Фото готового блюда')),
                ('cooking_time', models.PositiveSmallIntegerField(help_text='Задайте время приготовления блюда', validators=[django.core.validators.MinValueValidator(1, message='Укажите время больше нуля!')], verbose_name='Время приготовления')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveSmallIntegerField(help_text='Введите количество единиц ингредиента', validators=[django.core.validators.MinValueValidator(1, message='Укажите количество больше нуля!')], verbose_name='Количество')),
            ],
            options={
                'verbose_name': 'Ингредиент в рецепте',
                'verbose_name_plural': 'Ингредиенты в рецепте',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название тега', max_length=40, unique=True, verbose_name='Название')),
                ('color', recipes.fields.HexColorField(help_text='Выберите цвет', max_length=7, null=True, unique=True, verbose_name='HEX-код цвета')),
                ('slug', models.SlugField(help_text='Придумайте уникальный URL адрес для тега', unique=True, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='ShoppingList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shopping_recipe', to='recipes.Recipe', verbose_name='Рецепт')),
            ],
            options={
                'verbose_name': 'Список покупок',
                'verbose_name_plural': 'Списки покупок',
                'ordering': ('-id',),
            },
        ),
    ]
