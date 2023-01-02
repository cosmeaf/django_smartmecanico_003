from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,TokenVerifyView,TokenBlacklistView,)
from rest_framework import routers

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

#################################################################
# IMPORT VIEWS
from api.views.calibrateTireView import CalibrateTireModelViewSet
from api.views.fineTrafficView import FineTrafficModelViewSet
from api.views.financingView import FinancingModelViewSet
from api.views.insuranceView import InsuranceModelViewSet
from api.views.ipvaView import IpvaModelViewSet
from api.views.maintenanceView import MaintenanceModelViewSet
from api.views.supplyView import SupplyModelViewSet
from api.views.hourAvalibility import HourAvailibility
from api.views.hourServiceView import HourServiceModelViewSet
from api.views.scheduleView import ScheduleModelViewSet
from api.views.serviceView import ServiceModelViewSet
from api.views.vehicleView import VehicleModelViewSet
from api.views.addressView import AddressModelViewSet
from api.views.profileView import ProfileModelViewSet
from api.views.userRegisterView import UserRegisterView
from api.views.userView import UserViewSet

# ROUTERS
router = routers.DefaultRouter()
router.register(r'calibrate-tire', CalibrateTireModelViewSet, basename='calibrate-tire')
router.register(r'fine-traffic', FineTrafficModelViewSet, basename='fine-traffic')
router.register(r'financing', FinancingModelViewSet, basename='financing')
router.register(r'insurance', InsuranceModelViewSet, basename='insurance')
router.register(r'ipva', IpvaModelViewSet, basename='ipva')
router.register(r'maintenance', MaintenanceModelViewSet, basename='maintenance')
router.register(r'supply', SupplyModelViewSet, basename='supply')
router.register(r'hour-availability', HourAvailibility, basename='hour-availability')
router.register(r'hour-service', HourServiceModelViewSet, basename='hour-service')
router.register(r'schedule', ScheduleModelViewSet, basename='schedule')
router.register(r'service', ServiceModelViewSet, basename='service')
router.register(r'vehicle', VehicleModelViewSet, basename='vehicle')
router.register(r'address', AddressModelViewSet, basename='address')
router.register(r'profile', ProfileModelViewSet, basename='profile')
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/register/', UserRegisterView.as_view(), name='user_register'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('api/', include(router.urls)),
    path('api/', include('api.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
