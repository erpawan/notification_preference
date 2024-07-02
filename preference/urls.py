from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotificationTypeViewSet, NotificationPreferenceViewSet

router = DefaultRouter()
router.register(r'notification-types', NotificationTypeViewSet)
router.register(r'notification-preferences', NotificationPreferenceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
