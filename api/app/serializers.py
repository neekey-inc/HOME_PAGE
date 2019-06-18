from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ("id", "uuid", "subject", "name", "email", "phone", "detail", "status", "deleted", "created_at", "modified_at")
