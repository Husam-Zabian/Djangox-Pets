from django.urls import path
from .views import PetListView, PetDetailView, PetCreateView, PetUpdateView, PetDeleteView

urlpatterns = [
    path('pet/', PetListView.as_view(), name='pet_list'),
    path('pet/<int:pk>/', PetDetailView.as_view(), name='pet_detail'),
    path('pet/create/', PetCreateView.as_view(), name='pet_create'),
    path('pet/<int:pk>/update/', PetUpdateView.as_view(), name='pet_update'),
    path('pet/<int:pk>/delete/', PetDeleteView.as_view(), name='pet_delete'),
]