from .views import Shipment, ShipmentDelete, ShipmentUpdate, ShipmentView, Tracking 

from django.urls import path

urlpatterns = [
    path('api/shipment', Shipment.as_view(), name='shipment'),
    path('api/shipmentView', ShipmentView.as_view(), name='shipment_view'),
    path('api/shipmentUpdate/<tracking>', ShipmentUpdate.as_view(), name='shipment_update'),
    path('api/shipmentDelete/<tracking>', ShipmentDelete.as_view(), name='shipment_delete'),
    path('api/tracking/<tracking>', Tracking.as_view(), name='tracking'),

]