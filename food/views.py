from django.forms import BaseModelForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'food_items'

class DetailClassView(DetailView):
    model = Item
    template_name = 'food/detail.html'

class CreateItemView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'food/item-form.html'
    success_url = reverse_lazy('food:index')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user_name = self.request.user
        return super().form_valid(form)

class UpdateItemView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'food/item-form.html'

    success_url = reverse_lazy('food:index')

class DeleteItemView(DeleteView):
    model = Item
    template_name = 'food/delete_item.html'

    success_url = reverse_lazy('food:index')

