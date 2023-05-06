from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import AddressSerializer, UserProfileSerializer,LoginSerializer,ProductSerializer
from account.models import UserProfile,Address
from django.contrib.auth import authenticate
from utils import generateJWT
from product.models import Product,Category
from rest_framework import viewsets

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

@api_view(['GET'])
def getProducts(request):
    allProducts = None
    if("type" in request.GET and request.GET['type'] == 'all'):
        allProducts = Product.objects.all()
    
    elif("type" in request.GET and request.GET['type'] == 'topdeal'):
        allProducts = Product.getDiscountedProduct()
    
    if("category" in request.GET):
        print("Category is present",request.GET['category'])
        category = Category.objects.get(name=request.GET['category'])
        allProducts = Product.objects.filter(category = category)
    
    
    serializer = ProductSerializer(allProducts,many=True)
    return Response({"Product":serializer.data})


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get','post']
    action_serializers = {
        'retrieve':AddressSerializer,
        'list': AddressSerializer,
        'update': AddressSerializer,
        'delete':AddressSerializer,
    }
    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            return self.action_serializers.get(self.action, self.serializer_class)

        return super(AddressViewSet, self).get_serializer_class()

    