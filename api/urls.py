from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes),
    path('notes/' , views.getnotes),
    path('notes/create/',views.createNote),
    path('notes/<str:pk>' , views.getnote),
    path('notes/<str:pk>/update' , views.updateNote),
    path('notes/<str:pk>/delete' , views.deleteNote),



]