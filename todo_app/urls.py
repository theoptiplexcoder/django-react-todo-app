from django.urls import path
from . import views


urlpatterns=[
    path('user-register/',views.UserAuthView.as_view(),name="register"),
    path('user-login/',views.UserAuthView.as_view(),name="register"),
    path('user-todos/',views.UserTodoListView.as_view()),
    path('user-todos/<int:id>/',views.UserTodoListView.as_view()),

]
