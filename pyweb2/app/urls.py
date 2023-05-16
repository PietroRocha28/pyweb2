from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.home, name='home'),
    path("form", views.form, name='form'),
    path("editar/<int:id>",views.editar,name='edit'),
    path("deletar/<int:id>",views.deletar,name='deletar'),
]