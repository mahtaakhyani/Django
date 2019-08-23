from django.shortcuts import render
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

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
