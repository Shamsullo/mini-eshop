from django.contrib import admin
# from .models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

User = get_user_model()

# class UserAdmin(BaseUserAdmin):
#     search_fields = ('email', 'name',)
#     list_filter = ('is_admin',)
#     list_display = ('name', 'email', 'is_admin',)
#     fieldsets = (
#         (None, {'fields':('email', 'password',)}),
#         ('Personal info', {'fields': ('name',)}),
#         ('Permissions', {'fields': 'is_admin', 'is_active', 'is_staff'}),
#     )
#     ordering = ('id',)
#     # add_fieldsets = ()
#     filter_horizontal = ()
    
#     # class Meta:
#         # model = User

# # Register your models here.

admin.site.register(User)

admin.site.site_title = "Gettik Administration Panel"
admin.site.site_header = "Gettik Administration Panel"