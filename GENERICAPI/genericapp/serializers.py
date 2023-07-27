from .models import Info, Address
from rest_framework import serializers


class AddressSerializers(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ['house_no', 'lane_name', 'area_name', 'city']


class InfoSerializers(serializers.ModelSerializer):
    city = AddressSerializers(read_only=True)

    class Meta:
        model = Info
        fields = ['id', 'fname', 'lname', 'phoneno', 'city']

    def validate_fname(self, value):
        if len(value) <= 2:
            return serializers.ValidationError("First Name is too short")

        if not value.isaplha():
            return serializers.ValidationError('First Name should have only alphabets')

        return value

    def validate_lname(self, value):
        if len(value) <= 2:
            return serializers.ValidationError("Last Name is too short")

        if not value.isaplha():
            return serializers.ValidationError('Last Name should have only alphabets')

        return value

    def validate_phoneno(self, value):
        if len(value) < 10:
            return serializers.ValidationError("Phone no should be not be less than 10 digits")

        if len(value) > 10:
            return serializers.ValidationError("Phone no should be not be more than 10 digits")

        if not value.isdigit():
            return serializers.ValidationError('Phone no should have only digits')

        return value

