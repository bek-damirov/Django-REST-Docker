
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from accounts import views as acc_view


schema_view = get_schema_view(
   openapi.Info(
      title="picaby-0.0.0.0.1",
      default_version='v-0.0.0001',
      description="API для постов и комментов",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="bek@gmail.com"),
      license=openapi.License(name="No Licence"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


acc_router1 = DefaultRouter()
acc_router1.register('register', acc_view.AuthorRegisterAPIView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('api/accounts/', include(acc_router1.urls)),

    path('api/', include('posts.urls')),

    # documentation URL
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger_doc'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc_doc'),
]

