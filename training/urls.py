from django.urls import path
from . import views
from .views import (
    TrainingCreate, TrainingUpdate
)


urlpatterns = [
    path('', views.TrainingListView.as_view(), name='home'),
    # path('new-training/', views.new_training, name='new-training'),
    # path('trainings/<int:pk>/edit/', views.edit_training, name='edit-training'),
    path('delete-training/<int:pk>/', views.delete_training, name='delete_training'),
    path('pdf/', views.GeneratePDF.as_view(), name='generate_pdf'),
    path('create/', TrainingCreate.as_view(), name='new-training'),
    path('update/<int:pk>/', TrainingUpdate.as_view(), name='edit-training'),
    # path('create-training/', views.create_training, name='create-training'),
    # path('update-training/<int:pk>/', views.update_training, name='update-training')

]
