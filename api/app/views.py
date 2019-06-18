from rest_framework import viewsets
from .serializers import ContactSerializer
from .models import Contact
# from django.contrib.auth import authenticate
# from django.db import transaction
# from django.http import HttpResponse, Http404


class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    # send_notification(Contact.objects, '登録')
    queryset = Contact.objects.all()