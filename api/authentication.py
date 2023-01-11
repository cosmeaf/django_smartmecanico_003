from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
User = get_user_model()

class Email_OR_Username(BaseBackend):
  def get_user(self, user_id: int):
    try:
      return User.objects.get(pk=user_id)
    except User.DoesNotExist:
      return None
  
  def authenticate(self, request, username=None, password=None):
    UserModel = get_user_model()
    try:
      # user = UserModel.objects.get(Q(username__iexact=username)|Q(email__iexact=username))
      user = UserModel.objects.get(Q(email__iexact=username))
      if user.check_password(password):
        return user
    except UserModel.DoesNotExist:
      return None