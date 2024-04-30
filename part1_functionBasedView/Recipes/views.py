from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe
from .forms import RecipeForm


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, "recipe_list.html", {"recipes": recipes})


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, "recipe_detail.html", {"recipe": recipe})


def recipe_create(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect("recipe_list")
        else:
            print("not valid")
    else:
        form = RecipeForm()
    return render(request, "recipe_form.html", {"form": form})


def recipe_update(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("recipe_detail", pk=pk)  # Redirect to recipe detail page after update
    else:
        form = RecipeForm(instance=recipe)
    return render(request, "recipe_update.html", {"form": form})


def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        recipe.delete()
        return redirect("recipe_list")
    return render(request, "recipe_confirm_delete.html", {"recipe": recipe})
