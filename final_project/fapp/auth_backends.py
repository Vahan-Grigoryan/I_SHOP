from django.contrib.auth.backends import BaseBackend
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from fapp.models import User


class AuthWithEmailAndPasswordOnly(BaseBackend):
    """
    Auth backend for login by email and password,
    used for login in admin panel and in main site
    """
    def authenticate(self, request, **credentials):
        if 'username' in credentials:
            credentials['email'] = credentials.pop('username')

        try:
            user = User.objects.get(email=credentials['email'])
            passed = user.check_password(credentials['password'])
            if not passed:
                raise ValidationError('Не найдено активной учетной записи с указанными данными')
        except User.DoesNotExist:
            return

        return user

    def get_user(self, user_id):
        return User.objects.get(id=user_id)
