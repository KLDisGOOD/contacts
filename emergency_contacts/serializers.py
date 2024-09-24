from rest_framework import serializers
from .models import Contact
import re

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'first_name', 'last_name', 'phone_number']

    def validate_first_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("First name must contain only letters")
        return value
    
    def validate_last_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Last name must contain only letters")
        return value

    def validate_phone_number(self, value):
        # Regex pattern to check that phone number starts with + followed by country code and digits
        pattern = re.compile(r'^\+\d{1,3}\d{7,14}$')
        if not pattern.match(value):
            raise serializers.ValidationError("Phone number must be in correct format")
        return value
