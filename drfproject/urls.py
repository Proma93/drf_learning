"""
URL configuration for drfproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# drfproject/urls.py
from django.urls import path, include, re_path
from django.contrib import admin

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static

# === Common metadata ===
BASE_API_INFO = {
    "description": "API for managing Todos and TimingTodos",
    "contact": openapi.Contact(email="ahmed.farjana@gmail.com"),
    "license": openapi.License(name="MIT"),
}

# === Helper for building schema views ===
def build_schema_view(version, patterns):
    return get_schema_view(
        openapi.Info(
            title=f"Task Track API Documentation ({version})",
            default_version=version,
            **BASE_API_INFO,
        ),
        public=True,
        permission_classes=(permissions.IsAuthenticated,),  # or AllowAny for docs
        patterns=patterns,
    )

# import url patterns of the home app and wrap for versioned docs
v1_patterns = [
    path('', include('home.urls')),
    path('token/', obtain_auth_token),
]

schema_view_v1 = build_schema_view('v1', v1_patterns)

v2_patterns = [
    path('', include('home.urls')),
    path('token/', obtain_auth_token),
]

schema_view_v2 = build_schema_view('v2', v2_patterns)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # API versions
    path("api/v1/", include((v1_patterns, "v1"), namespace="v1")),
    path("api/v2/", include((v2_patterns, "v2"), namespace="v2")),

    # Versioned swagger endpoints
    re_path(r'^api/v1/swagger(?P<format>\.json|\.yaml)$', schema_view_v1.without_ui(cache_timeout=0), name='schema-json-v1'),
    path('api/v1/swagger/', schema_view_v1.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui-v1'),
    path('api/v1/redoc/', schema_view_v1.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),
    
    re_path(r"^api/v2/swagger(?P<format>\.json|\.yaml)$", schema_view_v2.without_ui(cache_timeout=0), name="schema-json-v2"),
    path("api/v2/swagger/", schema_view_v2.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui-v2"),
    path("api/v2/redoc/", schema_view_v2.with_ui("redoc", cache_timeout=0), name="schema-redoc-v2"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
