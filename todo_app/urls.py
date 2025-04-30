from django.urls import path
from . import views


urlpatterns=[
    path('user-register/',views.UserRegisterView.as_view(),name="register"),
    path('user-todos/',views.UserTodoListView.as_view(),name="user_todos")
]
