from rest_framework import serializers, viewsets
from .models import User, CustomerUser, DriverUser
from django.contrib.auth import authenticate

MIN_LENGTH = 8
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "phone", "license")

# Register Serializer

class CustomerRegisterSerializer(serializers.ModelSerializer):
    """ password = serializers.CharField(
        write_only = True,
        min_length = MIN_LENGTH,
        error_messages = {
            "min_length":"Password must be longer than {MIN_LENGTH} characters."
        }
    )

    confirm_password = serializers.CharField(
        write_only = True,
        min_length = MIN_LENGTH,
        error_messages = {
            "min_length":"Password must be longer than {MIN_LENGTH} characters."
        }
    )  """

    class Meta():
        model = User
        fields= "__all__"
        extra_kwargs = {'password': {'write_only': True}}
        
        
    
    """ def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("Password does not match.")
        return data """

    """ @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.username = self.cleaned_data.get('username')
        user.save()
        customer = CustomerUser.objects.create(user=user)
        customer.phone = self.cleaned_data.get('phone')
        customer.first_name = self.cleaned_data.get('first_name')
        customer.last_name = self.cleaned_data.get('last_name')
        customer.save()
        return user  """

    def create(self, validated_data):
        user =  super().create(validated_data)
        user.is_customer = True
        user.username = validated_data['username']
        user.set_password(validated_data['password'])
        user.save()
        customer = CustomerUser.objects.create(user=user)
        customer.username = validated_data['username']
        customer.email  = validated_data['email']
        customer.first_name = validated_data['first_name']
        customer.last_name =validated_data['last_name']
        customer.phone = validated_data['phone']
        
        customer.save()
        return user



class DriverRegisterSerializer(serializers.ModelSerializer):
    """ password = serializers.CharField(
        write_only = True,
        min_length = MIN_LENGTH,
        error_messages = {
            "min_length":"Password must be longer than {MIN_LENGTH} characters."
        }
    )

    confirm_password = serializers.CharField(
        write_only = True,
        min_length = MIN_LENGTH,
        error_messages = {
            "min_length":"Password must be longer than {MIN_LENGTH} characters."
        }
    )  """

    class Meta():
        model = User
        fields = "__all__"
        
    """ def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("Password does not match.")
        return data """

    def create(self, validated_data):
        user =  super().create(validated_data)
        user.is_driver = True
        user.username = validated_data['username']
        user.set_password(validated_data['password'])
        user.save()
        driver = DriverUser.objects.create(user=user)
        driver.email  = validated_data['email']
        driver.first_name = validated_data['first_name']
        driver.last_name =validated_data['last_name']
        driver.phone = validated_data['phone']
        if user.is_driver:
            driver.license = validated_data['license']
            driver.vehicle_number = validated_data['vehicle_number']
        driver.save()
        return user


class CustomerLoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            if User.objects.filter(username=username).exists():
                user = authenticate(request=self.context.get('request'),
                                    username=username, password=password)
                
                
            else:
                msg = {'detail': 'Username is not registered.',
                       'register': False}
                raise serializers.ValidationError(msg)

            if not user:
                msg = {
                    'detail': 'Unable to log in with provided credentials.', 'register': True}
                raise serializers.ValidationError(msg, code='authorization')

            if not user.is_customer:
                msg = {'detail': 'Username is not registered.',
                       'register': False}
                raise serializers.ValidationError(msg)
            

            
            
        else:
            msg = 'Must include "username" and "password".'
            raise serializers.ValidationError(msg, code='authorization')
        
        attrs['user'] = user
        return attrs

class DriverLoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            if User.objects.filter(username=username).exists():
                user = authenticate(request=self.context.get('request'),
                                    username=username, password=password)
            
            else:
                msg = {'detail': 'Username is not registered.',
                       'register': False}
                raise serializers.ValidationError(msg)

            if not user:
                msg = {
                    'detail': 'Unable to log in with provided credentials.', 'register': True}
                raise serializers.ValidationError(msg, code='authorization')

            if not user.is_driver:
                msg = {'detail': 'Username is not registered.',
                       'register': False}
                raise serializers.ValidationError(msg)

            if not user.is_approved:
                msg = {'detail': 'User is not approved.',
                   'register': False}
                raise serializers.ValidationError(msg)

            

        else:
            msg = 'Must include "username" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
