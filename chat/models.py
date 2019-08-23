from django.db import models
<<<<<<< HEAD
from user.models import *
from django.contrib.auth.models import User
from user.models import CustomUserModel
# Create your models here.



class Conversation(models.Model):
	chatname = models.CharField(max_length=100)
	members = models.ManyToManyField(CustomUserModel)
	is_group = models.BooleanField()

	def __str__(self):
		return self.chatname 





class Message(models.Model):
	user_id = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
	conversation_id = models.ForeignKey(Conversation, on_delete=models.CASCADE)
	text = models.TextField()
	date = models.DateField()


	def __str__(self):
		return self.text



# Message(user_id=Userlist.objects.filter(first_name='Mahta')[0],coversation_id =Conversation.objects.filter(chatname='test')[0],text = 'khoobi?',date=datetime.now()).save() 


# # show all texts in groups 'Mahta,id=1' joins, except her sent texts


# firstgroup = Conversation(chatname='First Group', is_group = True)
# secgroup = Conversation(chatname='Sec Group', is_group = True)















=======

# Create your models here.
>>>>>>> 0204819d1d498b7bd2a63d076d99142d295311fc
