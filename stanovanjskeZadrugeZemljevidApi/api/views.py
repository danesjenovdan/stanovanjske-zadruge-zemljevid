from django.shortcuts import render
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import uuid
import json
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError
from .models import Map, Message, Token
from .serializers import MapSerializer, MessageSerializer, TokenSerializer

# mailchimp vars
MAILCHIMP_LIST_ID = "3d0069f969"
MAILCHIMP_SEGMENT_ID = "4022841"
MAILCHIMP_SERVER = "us1"

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
                if token.used == False or token.admin_token == True:
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
                if not token.used or token.admin_token:
                    return Response({"status": "success"}, status=status.HTTP_200_OK)
        return Response({"status": "error"}, status=status.HTTP_200_OK)

    # def post(self, request):
    #     token_string = uuid.uuid4().hex
    #     new_token = Token(token = token_string, used = False)
    #     new_token.save()
    #     token_serializer = TokenSerializer(new_token)
    #     return Response({"status": "success", "data": token_serializer.data}, status=status.HTTP_200_OK)

class SubscribersView(APIView):
    # get number of subscribers
    def get(self, request):
        mailchimp = Client()
        mailchimp.set_config({
            "api_key": settings.MAILCHIMP_API_KEY,
            "server": MAILCHIMP_SERVER
        })
        try:
            response = mailchimp.lists.get_segment(list_id=MAILCHIMP_LIST_ID, segment_id=MAILCHIMP_SEGMENT_ID)
            return Response({"counter": response.get("member_count", -1)}, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class SubscriberView(APIView):
    # create new subscriber
    def post(self, request):
        newsletter = False
        email = ''
        name = ''

        params = json.loads(request.body)

        if params:
            # email is required
            if 'email' in params:
                email = params.get('email')
            else:
                return Response({"message": "no email in params"}, status=status.HTTP_400_BAD_REQUEST)
            # name is required
            if 'name' in params:
                name = params.get('name')
            else:
                return Response({"message": "no name in params"}, status=status.HTTP_400_BAD_REQUEST)
            # newsletter is not required
            if 'newsletter' in params:
                newsletter = params.get('newsletter')

        mailchimp = Client()
        mailchimp.set_config({
            "api_key": settings.MAILCHIMP_API_KEY,
            "server": MAILCHIMP_SERVER
        })
        try:
            response = mailchimp.lists.add_list_member(
                list_id=MAILCHIMP_LIST_ID,
                body={
                    "email_address": email,
                    "status": "subscribed",
                    "merge_fields": {
                        "MMERGE1": name
                    },
                    "interests": {
                        "a2c2bb7477": True,
                        "c44216baa3": newsletter
                    }
                }
            )

            # generate token
            token_string = uuid.uuid4().hex
            new_token = Token(token = token_string, used = False)
            new_token.save()
            token_serializer = TokenSerializer(new_token)

            return Response({"message": "member created", "data": token_serializer.data}, status=status.HTTP_200_OK)
        except ApiClientError as error:
            return Response({"message": error.text}, status=status.HTTP_400_BAD_REQUEST)
