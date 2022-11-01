from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('outings/', views.getOutings, name="outings"),
    path('outings/<str:pk/update', views.updateOuting, name="update-outing"),
    path('outings/<str:pk>/delete', views.deleteOuting, name="delete-outing"),
    path('outings/create/', views.createOuting, name="create-outing"),

    path('outings/<str:pk>/', views.getOuting, name="outing"),
]