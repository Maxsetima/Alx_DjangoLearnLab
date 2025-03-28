from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

# Get the custom user model (if any)
User = get_user_model()

# UserSerializer for displaying user details
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Using the custom user model
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']

# RegisterSerializer for user registration
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Creating user with password securely hashed using the custom manager
        user = User.objects.create_user(**validated_data)
        return user

# LoginSerializer for login with username and password
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

# UserRegistrationSerializer for detailed user registration with token
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, 
        required=True, 
        style={'input_type': 'password'}  # Hides the password input
    )
    token = serializers.CharField(read_only=True)  # Read-only token field

    class Meta:
        model = User  # Using the custom user model
        fields = ['id', 'username', 'email', 'password', 'token']

    def create(self, validated_data):
        # Create a user with the provided data (password is hashed)
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        # Create an auth token for the new user
        token = Token.objects.create(user=user)
        # Attach the token key to the response data
        validated_data['token'] = token.key
        return user
