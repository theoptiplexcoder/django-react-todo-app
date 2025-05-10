from django.urls import path
from . import views


urlpatterns=[
    path('user-register/',views.UserRegisterView.as_view(),name="register"),
    path('user-login/',views.UserLoginView.as_view(),name="login"),
    path('user-logout/',views.UserLogoutView.as_view(),name="logout"),
    path('user-todos/',views.UserTodoListView.as_view()),
    path('user-todos/<int:id>/',views.UserTodoListView.as_view()),

]
