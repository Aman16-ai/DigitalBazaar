from rest_framework import serializers
from django.contrib.auth.models import User
from account.models import UserProfile
from cart.models import Cart
from product.models import Product,Category

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = UserProfile
        fields = "__all__"
        
    def create(self, validated_data):
        user = validated_data.pop('user')
        print(user)
        userProfile = UserProfile.registerUser(username = user['username'],
                                               firstname = user['firstname'],
                                               lastname=user['lastname'],
                                               email = user['email'],
                                               password= user['password'],
                                               phone_no=validated_data['phone_no'],
                                               age = validated_data['age'],
                                               gender=validated_data['gender']
                                               )
        if userProfile is not None:
            cart = Cart.createCart(user=userProfile)
        return userProfile
    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
    
class ProductSerializer(serializers.ModelSerializer):
    # category = CategorySerializer() 
    class Meta:
        model= Product
        fields = "__all__"
        depth = True