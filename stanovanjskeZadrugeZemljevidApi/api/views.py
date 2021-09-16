from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Map, Message
from .serializers import MapSerializer, MessageSerializer

class MapView(APIView):
    def get(self, request):
        map = Map.objects.latest('id')
        map_serializer = MapSerializer(map)
        return Response({"status": "success", "data": map_serializer.data }, status=status.HTTP_200_OK)

    def post(self, request):
            map_serializer = MapSerializer(data=request.data)
            if map_serializer.is_valid():
                map_serializer.save()
                return Response({"status": "success", "data": map_serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"status": "error", "data": map_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class MessageView(APIView):
    def get(self, request):
        messages = Message.objects.all()
        message_serializer = MessageSerializer(messages, many=True)
        return Response({"status": "success", "data": message_serializer.data }, status=status.HTTP_200_OK)

    def post(self, request):
        message_serializer = MessageSerializer(data=request.data)
        if message_serializer.is_valid():
            message_serializer.save()
            return Response({"status": "success", "data": message_serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": message_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
