from django.urls import path
from . import views

urlpatterns = [
    path('', views.TrainingListView.as_view(), name='home'),
    path('new-training/', views.new_training, name='new-training'),
    path('trainings/<int:pk>/edit/', views.edit_training, name='edit-training'),
    path('delete-training/<int:pk>/', views.delete_training, name='delete_training'),
    path('pdf/', views.GeneratePDF.as_view(), name='generate_pdf'),

]
