from django.urls import path, include
from . import views

# this like app.use() in express
urlpatterns = [
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('notes', views.NoteList.as_view(), name="note_list"),
    path('notes/<int:pk>', views.NoteDetail.as_view(), name="note_detail"),
    path('users', views.Users.as_view(), name="user_list"),
    path('users/<int:pk>', views.UserInfo.as_view(), name="user_detail"),
    path('register', views.RegisterView.as_view(), name="auth_register")
]