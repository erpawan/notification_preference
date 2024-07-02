from django.db import models

# Create your models here.

class NotificationType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class NotificationPreference(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    notification_type = models.ForeignKey(NotificationType, on_delete=models.CASCADE)
    email = models.BooleanField(default=False)
    push = models.BooleanField(default=False)
    sms = models.BooleanField(default=False)
    frequency = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user} - {self.notification_type}"
