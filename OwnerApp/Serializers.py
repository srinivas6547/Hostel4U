from rest_framework.serializers import ModelSerializer
from OwnerApp.models import OwnerdataBase,HosteldataBase,RoomDataBase,HostellerDataBase
from  rest_framework import serializers
from django.contrib.auth.models import User



class OwnerDataSerializer(ModelSerializer):
    class Meta:
        model=OwnerdataBase
        fields ='__all__'
        
class HostelDataSerializer(ModelSerializer):
    class Meta:
        model=HosteldataBase
        fields='__all__'
class RoomDataSerializer(ModelSerializer):
    class Meta:
        model=RoomDataBase
        fields='__all__'

class HostellerDataSerializer(ModelSerializer):
    class Meta:
        model=HostellerDataBase
        fields='__all__'
        
        
        
