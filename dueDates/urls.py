from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = "list"),
    path('updateTask/<str:pk>/', views.updateTask, name = "updateTask"),
    path('deleteTask/<str:pk>/', views.deleteTask, name = "deleteTask")
]