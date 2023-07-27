from django.urls import path
from .views import AddressList, AddressDetails, InfoDetails, InfoList

urlpatterns = [
    path('info/', InfoList.as_view(), name='info-list'),
    path('info/<int:pk>', InfoDetails.as_view(), name='info-details'),
    path('address/<int:pk>', AddressDetails.as_view(), name='address-details'),
    path('address/', AddressList.as_view(), name='address-list'),
]