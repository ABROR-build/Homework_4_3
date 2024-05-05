from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_subjects, name='list_subjects'),
    path('lessons/<int:pk>/', views.list_lessons, name='list_lessons'),
    path('lesson/<int:pk>/', views.get_lesson, name='get_lesson'),
    path('lesson/add/', views.add_lesson, name='add_lesson'),
    path('lesson/edit/<int:pk>/', views.edit_lesson, name='edit_lesson'),
    path('lesson/delete/<int:pk>/', views.delete_lesson, name='delete_lesson')

]
