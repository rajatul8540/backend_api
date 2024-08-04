from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import register
from .serializers import LoginSerializrs
from django.contrib.auth.models import User
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny



@api_view(['GET','POST'])
# Create your views here.
@permission_classes([AllowAny])

def getLoginView(request):
    try:
      if request.method == 'POST':
         data = request.data
         serializer = LoginSerializrs(data= data)
         if serializer.is_valid():
            email = serializer.data['email']
            password = serializer.data['password']
            user= register.objects.filter(email=email).first()
            if user is None:
                
                return Response({'type':"FALSE",'message': "You are unauthorized user","value":[]}, status=400)
            else:
                if user.password != password:
                  return Response({'type':"FALSE",'message': "You are unauthorized user","value":[]}, status=400)
                else:
                    refresh = RefreshToken.for_user(user)
                    access_token = str(refresh.access_token)
                    return Response({'type':"TRUE",'message': "Login Successfully","value":[{"user_info":serializer.data, 'access_token':str(refresh.access_token)}]}, status=200)
                  
                return Response({'type':"FALSE",'message': "You are unauthorized user","value":[]}, status=400)   
            
         else:
                return Response({'type':"FALSE",'message': serializer.errors,"value":[]}, status=400)   
      else:
         return Response({'error': str(e)}, status=500)


    except Exception as e:
         return Response({'error': str(e)}, status=500)
        