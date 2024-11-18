from vehicle.apps import VehicleConfig
from rest_framework.routers import DefaultRouter
from vehicle.views import CarViewSet
app_name= VehicleConfig.name


router =DefaultRouter()
router.register(r"cars",CarViewSet,basename="cars")


urlpatterns = [
    # path("admin/", admin.site.urls),
    # path("",include("vehicle.url",namespace="vehicle")),

]+router.urls
