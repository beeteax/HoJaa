from rest_framework import serializers
from .models import RemoteInput

class RemoteInputSerializer(serializers.ModelSerializer):
    class Meta:
        model=RemoteInput
        fields=('TimeStamp','Text')
    
    
    