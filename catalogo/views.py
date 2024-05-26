from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView
from .models import Propiedad  # Import the Propiedad model
from django.views.generic import ListView, CreateView
from usuarios.models import CustomUser
from .forms import PropiedadForm   # Import the PropiedadForm form
from django.urls import reverse_lazy
from usuarios.permissions import verificar_limite_publicaciones
from django.core.exceptions import PermissionDenied
import logging
from django.db.models import Q
from .forms import BusquedaForm


class AnunciosView(ListView):
    model = Propiedad
    template_name = 'anuncios.html'
    context_object_name = 'propiedades'
    paginate_by = 6  # Número de propiedades por página
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('query')
        if query:
            queryset = queryset.filter(
                Q(direccion__icontains=query) | Q(descripcion__icontains=query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BusquedaForm(self.request.GET)
        return context

class DetallesCasaView(DetailView):
    model = Propiedad
    template_name = 'detalles.html'
    context_object_name = 'propiedad'
    pk_url_kwarg = 'propiedad_id'

class Vista360View(TemplateView):
    template_name = 'vista360.html'

class MisPublicacionesView(ListView):
    model = Propiedad
    template_name = 'mispublicaciones.html'
    context_object_name = 'propiedades'
    paginate_by = 3

    def get_queryset(self):
        # Obtenemos el usuario actual
        usuario = self.request.user
        # Filtramos las propiedades relacionadas con el usuario actual
        queryset = Propiedad.objects.filter(usuario=usuario)
        # Obtenemos el término de búsqueda
        query = self.request.GET.get('query')
        if query:
            # Filtramos las propiedades que coinciden con el término de búsqueda en nombre o descripción
            queryset = queryset.filter(
                Q(direccion__icontains=query) | Q(descripcion__icontains=query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BusquedaForm(self.request.GET)
        return context
    

    
logger = logging.getLogger(__name__)   

class NuevaPublicacion(LoginRequiredMixin, CreateView):
    model = Propiedad
    form_class = PropiedadForm
    template_name = 'nueva_publicacion.html'
    success_url = '/catalogos/mis_publicaciones/{{ request.user.username }}'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        try:
            verificar_limite_publicaciones(self.request.user)
        except PermissionDenied as e:
            logger.error(f"Permission denied: {e}")
            form.add_error(None, str(e))
            return self.form_invalid(form)
        
        response = super().form_valid(form)
        logger.info(f"Propiedad publicada por {self.request.user.username}")
        return response
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    