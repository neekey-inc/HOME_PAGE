from rest_framework import viewsets, generics, permissions
from .serializers import ContactSerializer
from .models import Contact
# from django.contrib.auth import authenticate
# from django.db import transaction
# from django.http import HttpResponse, Http404
import requests
import json



class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    # send_notification(Contact.objects, '登録')
    queryset = Contact.objects.all()


# SLACK_URL = "https://hooks.slack.com/services/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"

# def send_slack():
#     content = "GO!!GO!!"
#     payload = {
#         "text": content,
#         "icon_emoji": ':snake:',
#     }
#     data = json.dumps(payload)
#     requests.post(SLACK_URL, data)
# send_slack()