from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import UserProfileSerializer,LoginSerializer
from account.models import UserProfile
from django.contrib.auth import authenticate
from utils import generateJWT

@api_view(["POST"])
def register(request):
    serializer = UserProfileSerializer(data = request.data)
    if serializer.is_valid(raise_exception=ValueError):
        result = serializer.create(validated_data=request.data)
        print(result)
        token = generateJWT.generate(result.user)
    return Response({'message':UserProfileSerializer(result).data,"token":token})

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getUser(request):
    user = UserProfile.objects.get(user = request.user)
    s = UserProfileSerializer(user,many=False)
    return Response({"user":s.data})

@api_view(["POST"])
def loginUser(request):
    ls = LoginSerializer(data = request.data)
    if ls.is_valid(raise_exception=ValueError):
        data = ls.data
        user = authenticate(username = data['username'],password = data['password'])
        if user is not None:
            token = generateJWT.generate(user)
            return Response({"token":token})
    return Response({"message":"Something went wrong"})