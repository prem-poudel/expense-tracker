from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

api_prefix: str = "api"

urlpatterns = [
    path("admin/", admin.site.urls),
    path(f"schema/", SpectacularAPIView.as_view(), name="schema"),
    path("", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),

    path(
        f"{api_prefix}/",
        include([
            path(
                "v1/",
                include([
                    path("auth/", include("src.apps.auth.urls")),       # Authentication URLs
                    path("expenses/", include("src.apps.expenses.urls")),   # Expenses URLs
                ]),
            ),
        ]),
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)