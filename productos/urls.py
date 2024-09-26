# productos/urls.py
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, RolesViewSet,PaisViewSet  # Asegúrate de importar tus ViewSets

# Registrar los ViewSets
router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)  # Rutas para los usuarios
router.register(r'roles', RolesViewSet, basename='roles')  # Rutas para los roles
router.register(r'paises', PaisViewSet, basename='paises')  # Registrar el ViewSet para Países


urlpatterns = [
    path('', include(router.urls)),  # Incluir las rutas del router
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
