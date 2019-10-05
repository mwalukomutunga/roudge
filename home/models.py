from django.db import models
from datetime import datetime
from django.core.validators import FileExtensionValidator

# Create your models here.


class Videos(models.Model):
    title = models.CharField(max_length=200)
    url = models.FileField(
        upload_to='videos/', validators=[FileExtensionValidator(allowed_extensions=['mp4', 'webm', 'm4a', 'm4v', 'f4v', 'f4a', 'm4b', 'm4r', 'f4b', 'mov', '3gp', '3gp2', '3g2', '3gpp', '3gpp2'])])
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Videos'
