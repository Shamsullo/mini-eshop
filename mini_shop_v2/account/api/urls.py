from django.urls import path
from account.api.views import(
    registration_view,
    ObtainAuthTokenView,
    user_properties_view,
    update_user_view,
    does_account_exist_view,
    ChangePasswordView,
    logout_view,
    user_list_view,
)
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('check-if-account-exists', does_account_exist_view, name="check_if_account_exists"),
    path('change-password', ChangePasswordView.as_view(), name="change-password"),
    path('properties', user_properties_view, name="user-properties"),
    path('properties/update', update_user_view, name="user-update"),
    path('login', ObtainAuthTokenView.as_view(), name="login"), 
    path('logout', logout_view, name="logout"), 
    path('register', registration_view, name="user-registerion"),
    path('user-list', user_list_view, name="user-list"),
]