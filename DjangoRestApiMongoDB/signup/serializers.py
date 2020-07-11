from rest_framework import serializers
from signup.models import SignUp

class SignupSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = SignUp
        fields = ('id',
                  'username',
                  'email',
                  'password',)