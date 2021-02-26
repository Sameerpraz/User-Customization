from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class UserAdmin(UserAdmin):
    model = User
    list_display = ('first_name','email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff','is_superuser' ,'is_active')}),
    )
    """
    The parent class (django.contrib.auth.admin.UserAdmin) has an add_fieldsets 
    attribute that includes the username field. Add an attribute to your MyUserAdmin class 
    called add_fieldsets and treat it like the fieldsets attribute: 
    use it to define fields you want to show in the add form
    """

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name','last_name','email', 'password1', 'password2', 'is_staff','is_superuser'  ,'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, UserAdmin)