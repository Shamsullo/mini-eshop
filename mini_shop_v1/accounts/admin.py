from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin

from .models import MyUser, UserProfile

# Register your models here.
# from .forms import CreateUserForm

# class MyUserAdmin(UserAdmin):
#     add_form = CreateUserForm
#     # form = MyUserChangeForm
#     model = MyUser
#     list_display = ('first_name', 'email', 'is_staff', 'is_active',)
#     list_filter = ('email', 'is_staff', 'is_active',)
#     search_fields = ('first_name',)
#     ordering = ('id',)


admin.site.register(MyUser)
admin.site.register(UserProfile)