from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin
from api.models.profile import Profile
from api.models.address import Address
from api.models.vehicle import Vehicle
from api.models.service import Service
from api.models.schedule import Schedule
from api.models.hourService import HourService

from django.contrib.auth.models import User

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'first_name', 'last_name')
    list_select_related = ('profile', )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)
      
    def delete(self, *args, **kwargs):
        """
        Delete Image From Media
        """
        storage, path = self.image.storage, self.image.path
        super(Profile, self).delete(*args, **kwargs)
        storage.delete(path)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Address Admin
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('cep', 'logradouro', 'complemento',
                    'bairro', 'localidade', 'created_at', 'updated_at', 'deleted_at', 'user')
    ordering = ['created_at']
    search_fields = ['cep', 'user']
    exclude = ['user', ]
    list_display_links = ('cep',)
    readonly_fields = ['user', 'created_at', 'updated_at', 'deleted_at']

    def usuario(self, instance):
        return f'{instance.user.get_full_name()}'

    def get_queryset(self, request):
        """
        Show result user by id
        """
        queryset = super(AddressAdmin, self).get_queryset(request)
        if (request.user.is_superuser):
            return queryset
        else:
            return queryset.filter(user_id=request.user)

    def save_model(self, request, obj, form, change):
        """
        Change Method for save Vehicle data on Database
        """
        obj.user = request.user
        super().save_model(request, obj, form, change)
        
# Vehicle Admin
@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'fuell', 'year', 'odomitter', 'plate', 'user')
    ordering = ['created_at']
    search_fields = ['plate']
    exclude = ['user', ]
    list_display_links = ('plate',)
    readonly_fields = ['created_at', 'updated_at']

    def usuario(self, instance):
        return f'{instance.user.get_full_name()}'
    """
    Show result user by id
    """

    def get_queryset(self, request):
        queryset = super(VehicleAdmin, self).get_queryset(request)
        if (request.user.is_superuser):
            return queryset
        else:
            return queryset.filter(user_id=request.user)

    """
    Change Method for save Vehicle data on Database
    """

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
        
# Service Admin
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    ordering = ['created_at']
    search_fields = ['name']
    exclude = ['user', ]
    list_display_links = ('name',)
    readonly_fields = ['created_at', 'updated_at', 'deleted_at']

    def image_tag(self, obj):
        return format_html('<img src="{0}", style="width: 40px;" />'.format(obj.image.url))

    def delete(self, *args, **kwargs):
        """
        Delete Image From Media
        """
        storage, path = self.image.storage, self.image.path
        super(Service, self).delete(*args, **kwargs)
        storage.delete(path)

    def get_queryset(self, request):
        """
        Show result user by id
        """
        queryset = super(ServiceAdmin, self).get_queryset(request)
        if (request.user.is_superuser):
            return queryset
        else:
            return queryset.filter(user_id=request.user)

    def save_model(self, request, obj, form, change):
        """
        Change Method for save Service data on Database
        """
        obj.user = request.user
        super().save_model(request, obj, form, change)

# Schedule Admin
@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('address', 'vehicle', 'service', 'hour', 'day', 'user')
    ordering = ['created_at']
    search_fields = ['day']
    exclude = ['user',]
    list_display_links = ('address', 'vehicle', 'service', 'day', 'user')
    readonly_fields = ['created_at', 'updated_at', 'deleted_at']

    def get_queryset(self, request):
        """
        Show result user by id
        """
        queryset = super(ScheduleAdmin, self).get_queryset(request)
        if (request.user.is_superuser):
            return queryset
        else:
            return queryset.filter(user_id=request.user)

    def save_model(self, request, obj, form, change):
        """
        Change Method for save Service data on Database
        """
        obj.user = request.user
        super().save_model(request, obj, form, change)

# Hour Avaliable

@admin.register(HourService)
class HourServiceAdmin(admin.ModelAdmin):
    list_display = ('hour', 'user')
    ordering = ['created_at']
    search_fields = ['hour']
    # exclude = ['user', ]
    list_display_links = ('hour',)
    readonly_fields = ['user', 'created_at', 'updated_at', 'deleted_at']

    def usuario(self, instance):
        return f'{instance.user.get_full_name()}'

    def get_queryset(self, request):
        """
        Show result user by id
        """
        queryset = super(HourServiceAdmin, self).get_queryset(request)
        if (request.user.is_superuser):
            return queryset
        else:
            return queryset.filter(user_id=request.user)

    def save_model(self, request, obj, form, change):
        """
        Change Method for save Vehicle data on Database
        """
        obj.user = request.user
        super().save_model(request, obj, form, change)

