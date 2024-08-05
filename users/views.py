from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import register
from .serializers import LoginSerializrs,RegisterSerializrs
from django.contrib.auth.models import User
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
# from rest_framework.permissions import IsAuthenticated




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



@api_view(['POST'])
@permission_classes([AllowAny])
def getUserView(request):
    data = request.data
    userlist =  register.objects.all()
    serilzer = RegisterSerializrs(userlist, many=True)
    if serilzer.data is None:
         return Response({"status":"FALSE","message":"Data Not Found","value":[]}, status=200)
    else:
         return Response({"status":"TRUE","message":"Data  Found Successfully","value":serilzer.data}, status=200)
     
@api_view(['POST'])
@permission_classes([AllowAny])
def editUserView(request):
    try:
        data = request.data
        user_id = data.get('id')
        if not user_id:
            return Response({'status': 'FALSE', 'message': 'User ID is required', 'value': []}, status=400)
        
        user = register.objects.filter(id=user_id).first()
        if user is None:
            return Response({'status': 'FALSE', 'message': 'User not found', 'value': []}, status=404)
        
        serializer = RegisterSerializrs(user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'TRUE', 'message': 'User updated successfully', 'value': serializer.data}, status=200)
        else:
            return Response({'status': 'FALSE', 'message': serializer.errors, 'value': []}, status=400)
    except Exception as e:
        return Response({'error': str(e)}, status=500)
    
@api_view(['POST'])
@permission_classes([AllowAny])
def createuserView(request):
    try:
        data = request.data
        email = data.get('emai')

        alreadyRegisteredEmail = register.objects.filter(email=email).first()
        if alreadyRegisteredEmail:
            return Response({
                'status': 'FALSE',
                'message': 'Email is already registered',
                'value': []
            }, status=400)
            
        serializer = RegisterSerializrs(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'TRUE', 'message': 'User updated successfully', 'value': serializer.data}, status=200)
        else:
            return Response({'status': 'FALSE', 'message': serializer.errors, 'value': []}, status=400)
    except Exception as e:
        return Response({'error': str(e)}, status=500)
