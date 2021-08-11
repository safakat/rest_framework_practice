
from django.db.models.base import Model
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from social.models import Profile


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password')
        extra_kwargs = {'password':{'write_only':True}}

    def create(self,validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

#Profile model serializer
class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

