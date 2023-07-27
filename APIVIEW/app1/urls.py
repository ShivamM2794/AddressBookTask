from django.urls import path
from .views import info_list, info_details, AddressListView, AddressDetailsView, Fakedata

urlpatterns = [
    path('infolist/', info_list, name='info-list'),
    path('addresslist/', AddressListView.as_view(), name='address-list'),
    path('info/<int:pk>/', info_details, name='info-details'),
    path('address/<int:pk>/', AddressDetailsView.as_view(), name='address-details'),
    path('fake', Fakedata.as_view(), name='fake')
]