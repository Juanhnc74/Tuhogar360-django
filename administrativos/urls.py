from django.urls import path
from .views import AdministrativosView

urlpatterns = [
      path('administrativos/', AdministrativosView.as_view(), name='administrativos'),     
]