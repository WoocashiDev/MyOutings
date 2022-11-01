from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('profiles/', views.getProfiles, name="profiles"),
    path('profiles/<str:pk>/update', views.updateProfile, name="update-profile"),
    path('profiles/<str:pk>/delete', views.deleteProfile, name="delete-profile"),
    path('profiles/create', views.createProfile, name="create-profile"),

    path('profiles/<str:pk>/', views.getProfile, name="profile")
]