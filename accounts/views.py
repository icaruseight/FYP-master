# Create your views here.
from lib2to3.pgen2 import driver
from urllib import response
from rest_framework import serializers, viewsets
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .models import User, CustomerUser
from .serializers import CustomerRegisterSerializer, DriverRegisterSerializer, CustomerLoginUserSerializer, DriverLoginUserSerializer, UserSerializer

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = CustomerRegisterSerializer
    model = CustomerUser
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        return Response({
        "user": CustomerRegisterSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class DriverRegisterAPI(generics.GenericAPIView):
    serializer_class = DriverRegisterSerializer
    model = User
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": DriverRegisterSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })



from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from knox.auth import TokenAuthentication

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = CustomerLoginUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        user_id_main=user.id
        user_name=user.username
        customer= User.objects.filter(username=user_name).values('username')
        customer_names=[User.objects.filter(username=a['username']).values('username','phone','first_name', "last_name", "email", "vehicle_number", "license") for a in customer]
        login(request, user)
        user_details = super(LoginAPI, self).post(request, format=None)
        user_details.data["user"]= customer_names
        return Response({"data":user_details.data})

       
class DriverLoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = DriverLoginUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        user_name=user.username
        driver= User.objects.filter(username=user_name).values('username')
        driver_names=[User.objects.filter(username=a['username']).values('username','phone','first_name', "last_name", "email", "vehicle_number", "license") for a in driver]
        login(request, user)
        user_details = super(DriverLoginAPI, self).post(request, format=None)
        user_details.data["user"]= driver_names
        return Response({"data":user_details.data})


class UpdateProfile(generics.GenericAPIView):
    serializer_class = UserSerializer
    model = User
    def get(self, request, username,*args, **kwargs):
        post= User.objects.get(username=username)
        print(post.first_name)
        data = request.data
        post.first_name = data.get('first_name', post.first_name)
        post.last_name = data.get('last_name', post.last_name)
        post.phone = data.get('phone', post.phone)
        post.email = data.get('email', post.email)
        post.save()
        return Response({"data":UserSerializer(post, context=self.get_serializer_context()).data}) 
        
class UserAPI(generics.RetrieveAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = CustomerRegisterSerializer

    def get(self):
        return self.request.user
# MIN_LENGTH = 8

# class UserSerializer(serializers.ModelSerializer):

#     password = serializers.CharField(
#         write_only = True,
#         min_length = MIN_LENGTH,
#         error_messages = {
#             "min_length":"Password must be longer than {MIN_LENGTH} characters."
#         }
#     )

#     password2 = serializers.CharField(
#         write_only = True,
#         min_length = MIN_LENGTH,
#         error_messages = {
#             "min_length":"Password must be longer than {MIN_LENGTH} characters."
#         }
#     )

#     class Meta:
#         model = User
#         fields = "__all__"
    
#     def validate(self, data):
#         if data["password"] != data["password2"]:
#             raise serializers.ValidationError("Password does not match.")
#         return data

#     def create(self, validated_data):
#         user = User.objects.create(
#             username=validated_data["username"],
#             email =validated_data["email"],
#             first_name = validated_data["first_name"],
#             last_name = validated_data["last_name"],
#         )

#         user.set_password(validated_data["password"])
#         user.save()

#         return user

# class UserViewSet(viewsets.ModelViewSet):

#     queryset = User.objects.all()
#     serializer_class = UserSerializer