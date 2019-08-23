<<<<<<< HEAD

import random
import uuid
from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail

from django.contrib.auth import authenticate , login
from django.contrib.auth.models import User
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from user.serializers import UsersSerializer, RequestGetSerializer, RequestLoginSerializer, RequestSignupSerializer, UserProfileEdit
from mychat.celery import email




class Signup(APIView):

	def post(self, request):
		serializer = RequestSignupSerializer(data=request.data)
		if serializer.is_valid():
			u = serializer.save()
			# print(serializer.data['email'])
			token = uuid.uuid4()
			u.token = token
			u.set_password(data['password'])
			u.save()
			email.delay(u.token)
			return Response({
				'message': 'your account have been created successfuly',
				'data': serializer.data
			})
		else:
			return Response(
				serializer.errors,
				status=status.HTTP_400_BAD_REQUEST
			)



def Emailverify(self,request):

			l = CustomUserModel.objects.get(token = userparameter)
			if len(l) == 0:
				return Response(
					{
						'Message' : 'Not a valid verification link'
					},
					status = status.HTTP_404_NOT_FOUND
					)
			else:
				l[0].verified = True
				return Response(
					{
						'Message' : 'Your account has been verified'
					},
					status = status.HTTP_200_OK
					)




class LoginView(APIView):

	def post(self, request):
		serializer = RequestLoginSerializer(data=request.data)
		if serializer.is_valid():

			u = authenticate(
				request,
				username=serializer.data['username'],
				password=serializer.data['password'])

			if u is None:
				return Response(
					{
						'message': 'There is not any account with this username'
					},
					status=status.HTTP_404_NOT_FOUND
				) 
			if u:
				if u.verified:
					login(request, u)
					return Response(
						{
							'message': 'Your account info is correct',
							'data': {
								'first_name': u.first_name,
								"id": u.id,
							}
						},
						status=status.HTTP_200_OK
					)
				else:
					return Response(
					{
						'message': 'Your account has not been verfied yet'
					},
					status=status.HTTP_400_BAD_REQUEST
				)

			else:
				return Response(
					{
						'message': 'Your username or password is wrong'
					},
					status=status.HTTP_404_NOT_FOUND
				)
		else:
			return Response(
				serializer.errors,
				status=status.HTTP_400_BAD_REQUEST
			)
class AllUsers(APIView):
	def get(self, request):
		all_users = User.objects.all()
		s = UsersSerializer(all_users, many=True)
		return Response(
			{
				'Users': s.data
			},
			status=status.HTTP_200_OK
		)
		



class ProfileEdit(APIView):
	def put(self , request):
		request_serializer = UserProfileEdit(data = request.data)
		if request_serializer.is_valid() and request_serializer.data['token']!= 0:
			auth_user = User.objects.filter(token = request_serializer.data['token'] )[0]
			if 'first_name' in request_serializer.data:
				auth_user.first_name = request_serializer.data['first_name']
				return Response(
					{
						"message" : 'Your profile edited successfuly'
					},
					status=status.HTTP_200_OK
				)
			if 'last_name' in request_serializer.data:
				auth_user.last_name = request_serializer.data['last_name']
				auth_user.save()

				return Response(
					{
						"message" : 'Your profile edited successfuly'
					},
					status=status.HTTP_200_OK
				)
			# if 'first_name' not in request_serializer.data and 'last_name' not in request_serializer.data:
			#   return Response(
			#       {
			#           "message" : 'first_name or last_name required'
			#       },
			#       status=status.HTTP_200_OK)
		else:
			return Response(
				request_serializer.errors,
				status=status.HTTP_400_BAD_REQUEST
			)







class UserListItemView(APIView):

	def get(self, request):
		request_serializer = RequestGetSerializer(data=request.GET)
		if request_serializer.is_valid():

			users = User.objects
			if 'first_name' in request_serializer.data:
				users = users.filter(
					first_name=request_serializer.data['first_name']
				)
			if 'last_name' in request_serializer.data:
				users = users.filter(
					last_name=request_serializer.data['last_name']
				)

			serializer = UsersSerializer(instance=users, many=True)
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

	def post(self, request):
		serializer = UsersSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()
		else:
			return Response(serializer.errors, status=400)

		return Response(
			{
				'data': serializer.data
			},
			status=status.HTTP_201_CREATED
		)
=======
from django.shortcuts import render
from django.http import HttpResponse

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
>>>>>>> 0204819d1d498b7bd2a63d076d99142d295311fc
