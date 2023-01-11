from django.urls import path, re_path
from api.views.emailApiView import EmailAPI

# app_name = "available-hour"

urlpatterns = [
   re_path('send-email/', EmailAPI.as_view()),
]