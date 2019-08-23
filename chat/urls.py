<<<<<<< HEAD
from django.urls import path, re_path
=======
from django.urls import path
>>>>>>> 0204819d1d498b7bd2a63d076d99142d295311fc

from . import views

urlpatterns = [
<<<<<<< HEAD
	# re_path('conversation/<userparameter>',views.Conversation_view),
    # path('chat/', views.conversation_messages),
    path('conversation/', views.Conversation_view.as_view()),
    path('message/', views.MessageListView.as_view()),
    re_path('verify/user/(?P<userparameter>\w{0,50})/$', views.Emailverify),

=======
    path('chat/', views.chat_list , name='chat_list'),
>>>>>>> 0204819d1d498b7bd2a63d076d99142d295311fc
]
