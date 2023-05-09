from django.contrib.auth.backends import BaseBackend
from django.core.exceptions import ObjectDoesNotExist
from fapp.models import User


class AuthWithFirstLastNamesOnly(BaseBackend):
    def authenticate(self, request, **credentials):
        try:
            user = User.objects.get(**credentials)
        except ObjectDoesNotExist:
            return
        return user

    def get_user(self, user_id):
        return User.objects.get(id=user_id)
