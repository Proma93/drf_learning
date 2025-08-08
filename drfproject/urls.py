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
from django.urls import path, include
from django.contrib import admin

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path

common_info = openapi.Info(
    title="Task Track API Documentation",
    default_version='v1',
    description="API for managing Todos and TimingTodos",
    contact=openapi.Contact(email="ahmed.farjana@gmail.com"),
    license=openapi.License(name="MIT"),
)

# A helper to build a schema view for a given version and patterns
def build_schema_view(version, patterns):
    return get_schema_view(
        openapi.Info(
            title=f"Task Track API Documentation ({version})",
            default_version=version,
            description="API for managing Todos and TimingTodos",
            contact=openapi.Contact(email="ahmed.farjana@gmail.com"),
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),   # change for prod
        patterns=patterns,  # only include the versioned paths
    )

# import url patterns of the home app and wrap for versioned docs
v1_patterns = [
    path('api/v1/', include('home.urls')),
    path('api/v1/token/', obtain_auth_token),
]

schema_view_v1 = build_schema_view('v1', v1_patterns)

urlpatterns = [
    path('api/v1/token/', obtain_auth_token, name='token'),
    path('api/v1/', include('home.urls')),
    path('admin/', admin.site.urls),

    # Versioned swagger endpoints
    re_path(r'^api/v1/swagger(?P<format>\.json|\.yaml)$', schema_view_v1.without_ui(cache_timeout=0), name='schema-json-v1'),
    path('api/v1/swagger/', schema_view_v1.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui-v1'),
    path('api/v1/redoc/', schema_view_v1.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
