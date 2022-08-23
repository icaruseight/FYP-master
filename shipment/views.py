from accounts.models import DriverUser
from .serializer import ShipSerializer
from .models import Ship, TrackingModel
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import generics, permissions
import uuid
# Create your views here.
class Shipment(generics.GenericAPIView):
    queryset = Ship.objects.all()
    serializer_class = Ship
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        tracking = uuid.uuid4()
        data = JSONParser().parse(request)
        serializer = ShipSerializer(data = data)
        if serializer.is_valid():
            serializer.save(user=request.user, tracking_number = tracking)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    def get(self, request, *args, **kwargs):
        posts = Ship.objects.all()
        

        serializer = ShipSerializer(posts, many=True)

        """  for d in serializer.data:
            if d['assigned_driver'] != None:
                driver = DriverUser.objects.get(user = d['assigned_driver'])
                driver. """
        return JsonResponse(serializer.data, safe=False)
    
    def patch(self, request, *args, **kwargs):
        tracking_no = request.data['tracking_number']
        posts = Ship.objects.filter(tracking_number = tracking_no)
        print(posts)
        serializer = ShipSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)

class ShipmentView(generics.GenericAPIView):
    queryset = Ship.objects.all()
    serializer_class = Ship
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        posts = Ship.objects.filter(user=request.user)
        serializer = ShipSerializer(posts, many=True)
        return JsonResponse({"data":serializer.data}, safe=False) 


class ShipmentUpdate(generics.GenericAPIView):
    queryset = Ship.objects.all()
    serializer_class = Ship
    permission_classes = [permissions.IsAuthenticated]
    def patch(self, request,tracking):
        posts = Ship.objects.get(tracking_number = tracking)
        posts.status = "On Way"
        posts.save()
        return JsonResponse({"data":posts.status}, safe=False)

class ShipmentDelete(generics.GenericAPIView):
    queryset = Ship.objects.all()
    serializer_class = Ship
    permission_classes = [permissions.IsAuthenticated]
    def delete(self, request, tracking):
        posts = Ship.objects.get(tracking_number = tracking)
        posts.delete()
        return JsonResponse({"data":"deleted"}, safe=False)


class Tracking(generics.GenericAPIView):
    queryset = TrackingModel.objects.all()
    serializer_class = Ship
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        posts = Ship.objects.get(tracking_number = kwargs['tracking'])
        print(posts.assigned_driver)
        if posts.assigned_driver != None:
            driver = DriverUser.objects.get(user = posts.assigned_driver)
            posts.phone = driver.phone
            posts.driver_name = driver.first_name 
            posts.save()
        return JsonResponse({"data":"sone"}, safe=False)