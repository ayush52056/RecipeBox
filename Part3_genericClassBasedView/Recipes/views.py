from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Recipe
from .forms import RecipeForm

class RecipeListView(ListView):
    model = Recipe
    template_name = "recipe_list.html"
    context_object_name = "recipes"

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipe_detail.html"
    context_object_name = "recipe"

class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "recipe_form.html"
    success_url = reverse_lazy("recipe_list")

class RecipeUpdateView(UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "recipe_update.html"
    context_object_name = "recipe"

    def get_success_url(self):
        return reverse_lazy("recipe_detail", kwargs={"pk": self.object.pk})

class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = "recipe_confirm_delete.html"
    success_url = reverse_lazy("recipe_list")
    context_object_name = "recipe"
