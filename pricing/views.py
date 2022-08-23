from django.shortcuts import render
from .serializer import PricingSerializer
from .models import Pricing
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import generics, permissions

# Create your views here.
class PriceView(generics.GenericAPIView):
    serializer_class = Pricing
    def get(self, request, *args, **kwargs):
        posts = Pricing.objects.all()
        serializer = PricingSerializer(posts, many=True)
        return JsonResponse({"data": serializer.data},safe=False)
