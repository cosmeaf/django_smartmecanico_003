import os
import uuid
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    def get_file_path(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return os.path.join('profile', filename)
    
    user = models.OneToOneField(User, verbose_name='Usuário', on_delete=models.CASCADE)
    birthday=models.DateField('Aniversário',auto_now=False, null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,20}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField('Contato', validators=[phone_regex], max_length=17, blank=True, null=True)
    image = models.ImageField('Foto',default='default.png', 
                              upload_to=get_file_path, height_field=None, width_field=None, max_length=None, null=True, blank=True)
    
    class Meta:
        db_table = 'tbl_profile'
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        
    def __str__(self): 
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        if not hasattr(instance, "profile"):
            Profile.objects.create(user=instance)


post_save.connect(create_or_update_user_profile, sender=User)