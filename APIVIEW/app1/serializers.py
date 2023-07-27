from .models import Info, Address
from rest_framework import serializers

class InfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = "__all__"


class AddressSerializers(serializers.ModelSerializer):
    city = InfoSerializers(read_only=True)
    class Meta:
        model = Address
        fields = ['house_no', 'lane_name', 'area_name', 'city']


