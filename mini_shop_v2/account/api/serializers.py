from rest_framework import serializers
from account.models import User

class RegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'password2', "phone_number"]
        extra_kwargs = {
                'password': {'write_only': True},
        }	


    def	save(self):
        user = User(
                    name=self.validated_data['name'],
                    email=self.validated_data['email'],
                    phone_number=self.validated_data['phone_number']
                )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user


class UserPropertiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'name', 'email', "phone_number", "is_admin", "is_active"]


class ChangePasswordSerializer(serializers.Serializer):

    old_password 				= serializers.CharField(required=True)
    new_password 				= serializers.CharField(required=True)
    confirm_new_password 		= serializers.CharField(required=True)
