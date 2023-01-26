from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('workers/', views.workers, name='workers'),
    path('workers/details/<int:id>', views.details, name='details'),
    path('workers/delete/<int:id>', views.delete, name='delete'),
    path('workers/add_worker/', views.add_worker, name='add_worker'),
    path('workers/details/edit_worker/<int:id>', views.edit_worker, name='edit_worker'),

]
