from django.contrib import admin
from django.urls import path
from .views import orientador_list

urlpatterns = [
    path('list/', orientador_list, name="orientador_list"),  # name apelido dados ao liente
]
