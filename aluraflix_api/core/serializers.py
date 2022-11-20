from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'password2')
        read_only_fields = ('id',)
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        return User.objects.create_user(
            email=validated_data.get('email'), username=validated_data['username'], password=validated_data['password']
        )

    def validate(self, data):

        password1 = data['password']
        password2 = data['password2']

        if password1 and password2 and password1 != password2:
            raise serializers.ValidationError(detail='The two password fields didn’t match.', code='password_mismatch')

        validate_password(password1, self.instance)

        return data
