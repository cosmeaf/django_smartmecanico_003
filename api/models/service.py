from django.db import models
from api.models.base import Base
import uuid
import os

class Service(Base):  
    def get_file_path(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return os.path.join('icon', filename)
    
    # image = models.ImageField('Image', upload_to=get_file_path, height_field=None, width_field=None, max_length=None, null=True, blank=True)
    name = models.CharField('Titulo', max_length=255, editable=True)
    description = models.TextField('Descrição', editable=True)
    isFavorited = models.BooleanField('Favoritos', default=False)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return f'{self.name}'