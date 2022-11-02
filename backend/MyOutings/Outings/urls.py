from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('outings/', views.getOutings, name="outings"),
    path('outings/<str:pk>/update/', views.updateOuting, name="update-outing"),
    path('outings/<str:pk>/delete/', views.deleteOuting, name="delete-outing"),
    path('outings/create/', views.createOuting, name="create-outing"),

    path("outings/<str:pk>/expenses/", views.getExpenses, name="expenses"),
    path("outings/<str:pk>/expenses/create/", views.createExpense, name="create-expense"),
    path("outings/<str:pk>/expenses/<str:expense_id>/update/", views.updateExpense, name="update-expense"),
    path("outings/<str:pk>/expenses/<str:expense_id>/delete/", views.deleteExpense, name="delete-expense"),


    path("outings/<str:pk>/expenses/<str:expense_id>/", views.getExpense, name='expense'),
    path('outings/<str:pk>/', views.getOuting, name="outing"),
]