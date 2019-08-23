# from user.models import Userlist
from chat.models import *
from user.serializers import *
from rest_framework import serializers
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist






class NewConversationserializer(serializers.ModelSerializer):

    members = ShortUserProfileSerializer(many=True)

    class Meta:
        model = Conversation
        fields = ['chatname' ,'is_group' , 'members']




class ResponseMessageListSerializer(serializers.ModelSerializer):
    
    user_id = UserProfileSerializer()
    conversation_id = NewConversationserializer()

    class Meta:
        model = Message
        fields = '__all__'



class Allconversationserializer(serializers.ModelSerializer):

    class Meta:
        model = Conversation
        fields = '__all__'




class Allmessageserializer(serializers.Serializer):

    conversation_id = serializers.IntegerField()

    def validate(self,data):
        try:
            massage = Message.objects.filter(conversation_id = data['conversation_id'])
        except ObjectDoesNotExist:
            raise serializers.ValidationError('There is not any conversation with this id!')
        return data
class Allmessageview(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['user_id','text']



class Messageserializer(serializers.ModelSerializer):

    conversation_id = Allconversationserializer()

    class Meta:
        model = Message
        fields = ['id']




class Newmessageserializer(serializers.Serializer):
    text = serializers.CharField()
    conversation_id = serializers.IntegerField(
        min_value=1)

    def create(self, validated_data):
        c = Conversation.objects.get(
                id=validated_data['conversation_id'])
        m = Message(
            conversation_id=c,
            text=validated_data['text'],
            date=datetime.now(),
            user_id=self.context['user']
        )
        m.save()
        return m



class Editmessage(serializers.Serializer):
    message_id = serializers.IntegerField(min_value = 1)
    text = serializers.CharField(max_length = 200)

    def validate(self,data):
        try:
            message = Message.objects.get(id = data['message_id'])
        except objectDoesNotExist:
            raise serializers.ValidationError('id is wrong!')
        return data
    
    def update(self, message, valid_data ):
        message.text = valid_data.get('text', message.text)
        message.save()
        return message












	

# 	def create( self , validated_data):
# 		print("I'm in the create function")
# 		m = Message(
# 			# user_id = validated_data['user_id'],
# 			conversation_id = validated_data['conversation_id'],
# 			# text = validated_data['text'],
# 			# date = validated_data['date']
# 			)
# 		m.save()	

# 		return u






	# user_id = serializers.CharField(
	# 	required = True , allow_blank = False , max_length = 100
	# 	)
	# text = serializers.CharField(
	# 	required = True , allow_blank = False , max_length = 1000
	# 	)
	# date = serializers.DateField()
