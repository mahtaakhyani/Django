from django.urls import path, re_path, include

# from . import views
from . import views

urlpatterns = [
    # path('list/', views.user_list_view),
    # path('item/', views.UserListItem.as_view()),
    path('login/', views.LoginView.as_view()),
    path('signup/', views.Signup.as_view()),
    path('list/', views.AllUsers.as_view()),
    path('edit/', views.ProfileEdit.as_view()),

    # path('', include('django.contrib.auth.urls')), # new
]