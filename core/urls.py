from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

from core import views

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),  # raw OpenAPI JSON
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  # Swagger UI
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),  # ReDoc UI
    path('api/', include('api.urls', namespace='api')),
]
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('blogs/', include('blogs.urls', namespace='blogs')),
    path('products/', include('products.urls', namespace='products')),
    path('users/', include('users.urls', namespace='users')),
    path('', include('shared.urls', namespace='shared')),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = views.handler404
handler403 = views.handler403
handler500 = views.handler500