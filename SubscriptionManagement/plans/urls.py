from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlanViewSet, SubscriptionViewSet, EventViewSet

router = DefaultRouter()
router.register(r"plans", PlanViewSet)
router.register(r"Subscriptions", SubscriptionViewSet)
router.register(r"Events", EventViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
