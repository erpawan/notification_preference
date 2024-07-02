from rest_framework import viewsets
from .models import NotificationType, NotificationPreference
from .serializers import NotificationTypeSerializer, NotificationPreferenceSerializer

# Create your views here.

class NotificationTypeViewSet(viewsets.ModelViewSet):
    queryset = NotificationType.objects.all()
    serializer_class = NotificationTypeSerializer

class NotificationPreferenceViewSet(viewsets.ModelViewSet):
    queryset = NotificationPreference.objects.all()
    serializer_class = NotificationPreferenceSerializer
