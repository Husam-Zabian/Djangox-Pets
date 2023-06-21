from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Pet


class PetListView(ListView):
    template_name = "Pet/pet-list.html"
    model = Pet


class PetDetailView(DetailView):
    template_name = "Pet/pet-detail.html"
    model = Pet


class PetCreateView(CreateView):
    template_name = "Pet/pet-create.html"
    model = Pet
    fields = ['name','owner','desc','color']
    success_url = reverse_lazy("pet_list")

class PetUpdateView(UpdateView):
    template_name = "Pet/pet-update.html"
    model = Pet
    fields = ['name','owner','desc','color']
    success_url = reverse_lazy("pet_list")

class PetDeleteView(DeleteView):
    template_name = "Pet/pet-delete.html"
    model = Pet
    success_url = reverse_lazy("pet_list")