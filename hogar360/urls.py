from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('usuarios.urls')),
    path('administrativos/', include('administrativos.urls')),
    path('catalogos/', include('catalogo.urls')),
    path('blog/', include('blog.urls')),
    path('subscriptions/', include('subscriptions.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)