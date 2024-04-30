from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Recipe
from .forms import RecipeForm

class RecipeListView(View):
    def get(self, request):
        recipes = Recipe.objects.all()
        return render(request, "recipe_list.html", {"recipes": recipes})

class RecipeDetailView(View):
    def get(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        return render(request, "recipe_detail.html", {"recipe": recipe})

class RecipeCreateView(View):
    def get(self, request):
        form = RecipeForm()
        return render(request, "recipe_form.html", {"form": form})

    def post(self, request):
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("recipe_list")
        return render(request, "recipe_form.html", {"form": form})

class RecipeUpdateView(View):
    def get(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        form = RecipeForm(instance=recipe)
        return render(request, "recipe_update.html", {"form": form})

    def post(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("recipe_detail", pk=pk)
        return render(request, "recipe_update.html", {"form": form})

class RecipeDeleteView(View):
    def get(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        return render(request, "recipe_confirm_delete.html", {"recipe": recipe})

    def post(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        recipe.delete()
        return redirect("recipe_list")
