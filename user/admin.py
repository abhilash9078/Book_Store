from django.contrib import admin
from user.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserModelAdmin(BaseUserAdmin):

    list_display = ('id', 'email', 'username', 'mobile_no', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
       ('User Credentials', {'fields': ('email', 'password')}),
       ('Personal info', {'fields': ('username',)}),
       ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
           'classes': ('wide',),
           'fields': ('email', 'username', 'mobile_no', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email', 'id')
    filter_horizontal = ()


# Now register the new UserModelAdmin...
admin.site.register(User, UserModelAdmin)
