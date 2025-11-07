
from django.conf import settings
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombres_completos = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.nombres_completos or self.user.get_username()
