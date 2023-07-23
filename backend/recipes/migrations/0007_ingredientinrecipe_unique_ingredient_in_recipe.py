# Generated by Django 4.2.2 on 2023-07-20 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_remove_ingredientinrecipe_unique_ingredient_in_recipe'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='ingredientinrecipe',
            constraint=models.UniqueConstraint(fields=('ingredient', 'amount'), name='unique_ingredient_in_recipe'),
        ),
    ]