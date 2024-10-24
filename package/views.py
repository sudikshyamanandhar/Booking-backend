from django.shortcuts import render
from rest_framework import generics,permissions,mixins,status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import *
from .serializers import PackageSerializer,ReviewSerializer

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.db import IntegrityError
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

# Create your views here.

class Featured_list(generics.ListAPIView):
    queryset=Package.objects.all().order_by('-id')[:6]
    serializer_class=PackageSerializer

    def perform_create(self,serializer):
        serializer.save()

class PackageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer


class ReviewListCreate(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        package_id = self.kwargs['pk']
        return Review.objects.filter(package_id=package_id)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)