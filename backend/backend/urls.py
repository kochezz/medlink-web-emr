from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
# Temporarily comment out drf_yasg imports until packages are installed
# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi


# Temporarily comment out schema_view until drf_yasg is installed
# schema_view = get_schema_view(
#    openapi.Info(
#       title="MedLink EMR API",
#       default_version='v1',
#       description="MedLink Electronic Medical Record System",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="contact@medlink.local"),
#       license=openapi.License(name="BSD License"),
#    ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Temporarily comment out custom app URLs until apps are fixed
    # path('api/', include('users.urls', namespace='users')),
    # path('api/', include('records.urls', namespace='records')),
    # path('api/', include('patients.urls', namespace='patients')),
    
    # Temporarily comment out API documentation URLs
    # path(
    #     'swagger<format>/', schema_view.without_ui(cache_timeout=0),
    #     name='schema-json'
    #     ),
    # path(
    #     'swagger/', schema_view.with_ui('swagger', cache_timeout=0),
    #     name='schema-swagger-ui'
    #     ),
    # path(
    #     'redoc/',
    #     schema_view.with_ui('redoc', cache_timeout=0),
    #     name='schema-redoc'
    #     ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)