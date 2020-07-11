from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from signup.models import SignUp
from signup.serializers import SignupSerializer
from rest_framework.decorators import api_view

@api_view(['GET','POST','DELETE'])
def signup_list(request):
    
    if request.method == 'POST':
        signup_data = JSONParser().parse(request)
        signup_serializer = SignupSerializer(data=signup_data)
        
        if signup_serializer.is_valid():
            signup_serializer.save()
            return JsonResponse(signup_serializer.data, status = status.HTTP_201_CREATED)
        return JsonResponse(signup_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
