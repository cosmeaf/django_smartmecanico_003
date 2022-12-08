from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from api.models.profile import Profile
from django.contrib.auth import get_user_model
User = get_user_model()

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