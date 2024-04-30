from django.urls import path
from .views import (
    RecipeListView,
    RecipeDetailView,
    RecipeCreateView,
    RecipeUpdateView,
    RecipeDeleteView,
    SignupView,
    LoginView,
    LogoutView
)

urlpatterns = [
    path('', RecipeListView.as_view(), name='recipe_list'),
    path('<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('create/', RecipeCreateView.as_view(), name='recipe_create'),
    path('<int:pk>/update/', RecipeUpdateView.as_view(), name='recipe_update'),
    path('<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe_delete'),
    path('signup/', SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/",LogoutView.as_view(), name="logout"),
]
