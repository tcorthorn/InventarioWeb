
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from oficina import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('oficina.urls')),
    path('', RedirectView.as_view(url='/home/', permanent=True)),
    path('buscar/', views.buscar, name= 'buscar'),
    path('accounts/', include('django.contrib.auth.urls')),
]

# Use static() to add url mapping to serve static files during development (only)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
