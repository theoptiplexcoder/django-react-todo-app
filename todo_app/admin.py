from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Todo, CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('email', 'name')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2'),
        }),
    )

admin.site.register(Todo)
admin.site.register(CustomUser, CustomUserAdmin)
