from rest_framework.routers import DefaultRouter

from .views import DynastyView

router = DefaultRouter()
router.register('dynasty', DynastyView, basename='dynasty')

urlpatterns = router.urls
