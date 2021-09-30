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
        request_token = TokenSerializer(data=request.data)
        map_serializer = MapSerializer(data=request.data)
        if request_token.is_valid() and map_serializer.is_valid():
            try:
                token = Token.objects.get(token=request_token.validated_data.get('token'))
                if token.used == False:
                    map_serializer.save()
                    token.used = True
                    token.save()
                    return Response({"status": "success", "data": map_serializer.data}, status=status.HTTP_200_OK)
                else:
                    return Response({"status": "error", "data": "Token already used."}, status=status.HTTP_403_FORBIDDEN)
            except:
                return Response({"status": "error", "data": "Token does not exist."}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)

class MessageView(APIView):
    def get(self, request):
        messages = Message.objects.all()
        message_serializer = MessageSerializer(messages, many=True)
        return Response({"status": "success", "data": message_serializer.data }, status=status.HTTP_200_OK)

    def post(self, request):
        request_token = TokenSerializer(data=request.data)
        message_serializer = MessageSerializer(data=request.data)
        if request_token.is_valid() and message_serializer.is_valid():
            try:
                token = Token.objects.get(token=request_token.validated_data.get('token'))
                if token.used_message == False:
                    message_serializer.save()
                    token.used_message = True
                    token.save()
                    return Response({"status": "success", "data": message_serializer.data}, status=status.HTTP_200_OK)
                else:
                    return Response({"status": "error", "data": "Token already used."}, status=status.HTTP_403_FORBIDDEN)
            except:
                return Response({"status": "error", "data": "Token does not exist."}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)

class TokenView(APIView):
    def get(self, request):
        params = request.query_params
        if (params and params.get('token')):
            token_param = params.get('token')
            tokens = Token.objects.filter(token=token_param)
            if (len(tokens) > 0):
                token = tokens[0]
                if not token.used:
                    return Response({"status": "success"}, status=status.HTTP_200_OK)
        return Response({"status": "error"}, status=status.HTTP_200_OK)

    def post(self, request):
        token_string = uuid.uuid4().hex
        new_token = Token(token = token_string, used = False)
        new_token.save()
        token_serializer = TokenSerializer(new_token)
        return Response({"status": "success", "data": token_serializer.data}, status=status.HTTP_200_OK)

