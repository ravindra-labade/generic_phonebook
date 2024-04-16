
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Phonebook

class Add_view(CreateView):
    model = Phonebook
    fields = "__all__"


class List_view(ListView):
    model = Phonebook

class Detail_view(DetailView):
    model = Phonebook


class Update_view(UpdateView):
    model = Phonebook

    fields = "__all__"
    success_url = "/"

class Delete_view(DeleteView):
    model = Phonebook
    success_url = "/"
    template_name = "phone/phonebook_confirm.html"
