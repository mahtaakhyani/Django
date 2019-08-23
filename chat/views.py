<<<<<<< HEAD


from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist

=======
>>>>>>> 0204819d1d498b7bd2a63d076d99142d295311fc
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

<<<<<<< HEAD
from django.http.response import JsonResponse
from mychat.utils import CsrfExemptSessionAuthentication

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.authentication import BasicAuthentication 
from django.contrib.auth.models import AnonymousUser


from chat.serializers import *

from user.views import *
from user.models import *
from chat.models import *










class Conversation_view(APIView):
    def get(self, request):
        messages = Message.objects.all()
        serializer = ResponseMessageListSerializer(
                messages,
            many=True
        )
        return Response(
            {
                'data': serializer.data
            },
            status=status.HTTP_200_OK
        )

    def post(self, request):
        serializer = NewConversationserializer(data = request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                "Message" : "Group created succesfuly"
                }
                )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

class MessageListView(APIView):

    def get(self, request):
        request_serializer = Allmessageserializer(data = request.GET)
        if request_serializer.is_valid():
            messages = Message.objects.filter(conversation_id = request_serializer.data['conversation_id'])
            serializer = Allmessageview(
                messages,
                many=True
            )
            return Response(
                {
                    'data': serializer.data
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                request_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request):
        try:
            message = Message.objects.get(id = request.data['message_id'])
            serializer = Editmessage (message, data = request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        'message' : 'message edited succesfuly'
                    }
                    )
            else:
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST )
        except ObjectDoesNotExist:
           return Response({'message':'There is no message with this ID'}, status = status.HTTP_404_NOT_FOUND)


    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)

    def post(self, request):
        if type(request.user) is AnonymousUser:
            return Response({
                'message': 'Unauthorize!!!!'
            }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            serializer = Newmessageserializer(
                data=request.data,
                context={
                    'user': request.user
                }
            )
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        'message': 'Message saved!'
                    }
                )
            else:
                return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )

# class Message_view(APIView):
#     def get(self, request):
#         request_serializer = Allmessageserializer(data = request.GET)
#         if request_serializer.is_valid():
#             allmessages = Message.objects.filter(conversation_id = request_serializer.data['conversation_id'])

#             return Response(
#                 {
#                 "Messages in this id" : allmessages.data
#                 },
#                 status = status.HTTP_200_OK
#                 )
#         else:
#             return Response(
#                 request_serializer.errors,
#                 status = status.HTTP_400_BAD_REQUEST
#                 )


# def conversation_messages(request):
#     if request.method == 'GET' :
#         request_serializer = Messageserializer(data = request.GET) 

#         if request_serializer.is_valid():

#             messages = Message.objects
#             if 'conversation_id' in request_serializer.data:

#                 requested_messages = messages.filter(
#                     conversation_id = Messageserializer(data = request.GET)
#                     )

#                 return JsonResponse(
#                 {    

#                 'Messages' : requested_messages 

#                 }   
    

#                 )

#         else:
#             return JsonResponse(

#                 request_serializer.errors,
#                 status=400
#             )

































# new_message=[]
# def chat_list(request): 
#     if request.method == 'GET':
#         return render(
#             request,
#             'chat.html',
#             {
#                     "chat": new_message,
#                     "users": users
#             }
#         )

#     elif request.method == 'POST':
#     	# if chat(request.POST['messages'])== <QueryDict: {'messages': ['']}>
#         print('request.POST:', request.POST)
        

#         try:
#             new_message.append(Chat(request.POST['messages']))

#         except MultiValueDictKeyError :
#             pass	
        

#         return render(
#             request,
#             'chat.html',
#             {
#             	# conversation_id, #group_name
#             	# user_id, #sender
#                 "chat": new_message, #text
#                 "users": users, #all_contacts
#             },
#         )
    





# def Conversation_view(request, userparameter):
#     if request.method == 'GET':
#         pass

#     elif request.method == "POST":
#         try:
#             print(request.POST['messages'])
#             u = Userlist.objects.filter(first_name="Mahta").values('id')[0]
#             c = Conversation.objects.filter(
#                 id=int(userparameter)).values('id')[0]
#             Messages(
#                 user_id=u,
#                 conversation_id=c,
#                 text=request.POST['messages'],
#                 date=datetime.now()
#             ).save()
#         except ValueError:
#             print("there is no userparameters")
#         except MultiValueDictKeyError:
#         	pass


#     try:
#         messages = Message.objects.filter(
#             conversation_id=int(userparameter)
#         )
#     except ValueError:
#         messages =  []

#     return render(
#         request,
#         'chat.html',
#         {
#             "messages": messages,
#             "conversations": Conversation.objects.all(),
#             "users": users
#         }
#     )







=======
class User:
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
        # return self.first_name + ' ' + self.last_name

    def get_fullname(self):
        return "%s %s" % (self.first_name, self.last_name)

		


users = [
    User('Vahid', 'Kharazi'),
    User('Sara', 'Ahmadi'),
    User('Tarane', 'AliDoosti')
]


class chat:
	def __init__(self,message):
		self.message = message

	def __str__(self):
		return self.message



def chat_list(request):	
	chat = []
	new_message=''
	if request.method == 'GET':
		return render(request,'chat.html')

	elif request.method == 'POST':
	        # print('request.POST:', request.POST)
	        try:
	        	new_message += chat(request.POST['messages'])

	        except MultiValueDictKeyError :
	        	chat.append(new_message)	
	        	

	        return render(
	            request,
	            'chat.html',{chat}
	        )
	print(chat)
>>>>>>> 0204819d1d498b7bd2a63d076d99142d295311fc
