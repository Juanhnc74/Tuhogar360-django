from django.shortcuts import render
from django.views.generic import ListView
from usuarios.models import CustomUser

# Create your views here.
class AdministrativosView(ListView):
   model = CustomUser
   template_name = 'administrativos.html'
   context_object_name = 'list_usuarios'

   def get_queryset(self):
      return CustomUser.objects.all()
    
