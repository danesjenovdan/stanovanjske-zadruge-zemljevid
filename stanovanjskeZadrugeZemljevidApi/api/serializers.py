from rest_framework import serializers
from .models import Map, Message

class MapSerializer(serializers.ModelSerializer):
    map = serializers.JSONField()

    class Meta:
        model = Map
        fields = ('__all__')

class MessageSerializer(serializers.ModelSerializer):
    index = serializers.IntegerField()
    text = serializers.CharField()

    class Meta:
        model = Message
        fields = ('__all__')
