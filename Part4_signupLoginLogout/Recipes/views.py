from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,FormView,View
from .models import Recipe
from .forms import RecipeForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404

class SignupView(FormView):
    template_name = 'signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class LoginView(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('recipe_list')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('recipe_list')


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipe_list.html"
    context_object_name = "recipes"


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipe_detail.html"
    context_object_name = "recipe"

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "recipe_form.html"
    success_url = reverse_lazy("recipe_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "recipe_update.html"
    context_object_name = "recipe"

    def get_success_url(self):
        return reverse_lazy("recipe_detail", kwargs={"pk": self.object.pk})

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.owner or self.request.user.is_superuser

class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    template_name = "recipe_confirm_delete.html"
    success_url = reverse_lazy("recipe_list")
    context_object_name = "recipe"

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.owner or self.request.user.is_superuser