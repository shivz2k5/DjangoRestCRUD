from django.contrib import admin
from django.urls import path
from CRUD_User.views import userView, detailedUserView

urlpatterns = [
  path('users/', userView.as_view()),
  path('users/<int:pk>/', detailedUserView.as_view()),
]