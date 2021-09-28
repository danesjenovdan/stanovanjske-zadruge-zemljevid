from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import uuid
from .models import Map, Message, Token
from .serializers import MapSerializer, MessageSerializer, TokenSerializer

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

class TokenView(APIView):
    def post(self, request):
        token_string = uuid.uuid4().hex
        new_token = Token(token = token_string, used = False)
        new_token.save()
        token_serializer = TokenSerializer(new_token)
        return Response({"status": "success", "data": token_serializer.data}, status=status.HTTP_200_OK)
