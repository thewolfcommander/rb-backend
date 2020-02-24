from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.models import (
    Contact,
)
from core.api.serializers import (
    ContactSerializer,
)

# Create your views here.
class ContactCreateAPIView(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        qs = Contact.objects.all()
        serializer = ContactSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        