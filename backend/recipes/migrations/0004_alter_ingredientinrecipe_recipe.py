# Generated by Django 4.2.2 on 2023-07-20 12:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_ingredientinrecipe_ingredient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientinrecipe',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredientrecipes', to='recipes.recipe', verbose_name='Рецепт'),
        ),
    ]
