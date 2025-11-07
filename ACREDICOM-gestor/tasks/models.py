
from django.conf import settings
from django.db import models

class Task(models.Model):
    PRIORIDAD_CHOICES = [
        ('ALTA', 'Alta'),
        ('MEDIA', 'Media'),
        ('BAJA', 'Baja'),
    ]
    ESTADO_CHOICES = [
        ('ASIGNADO', 'Asignado'),
        ('EN_PROCESO', 'En proceso'),
        ('TERMINADO', 'Terminado'),
    ]

    titulo = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)
    fecha_vencimiento = models.DateField()
    prioridad = models.CharField(max_length=10, choices=PRIORIDAD_CHOICES, default='MEDIA')
    estado = models.CharField(max_length=12, choices=ESTADO_CHOICES, default='ASIGNADO')
    usuario_asignado = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tareas')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"{self.titulo} → {self.get_prioridad_display()}"
