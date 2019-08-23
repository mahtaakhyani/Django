from django.shortcuts import render
from django.http import HttpResponse

class User:
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

		


users = [
    User('Vahid', 'Kharazi'),
    User('Sara', 'Ahmadi'),
    User('Tarane', 'AliDoosti')
]


# def View_users(request):
#     return render(request,
#         'chat.html',
#         {
#         "users": users
#         }
#         )
