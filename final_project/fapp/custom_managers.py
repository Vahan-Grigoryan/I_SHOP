from django.contrib.auth.base_user import BaseUserManager

class MyUserManager(BaseUserManager):
    def create_user(self, first_name=None, last_name=None, password=None, **extra_kwargs):
        """If user creation from Google call default create_user() method, else custom method"""

        if all((first_name, last_name, password)):
            # common creation
            user = self.model(
                first_name = first_name,
                last_name = last_name,
                email = self.normalize_email(extra_kwargs.pop('email')),
                **extra_kwargs
            )
            user.set_password(password)
            user.save(using=self._db)
        else:
            # google creation
            user = self.model(**extra_kwargs)
            user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, password, **extra_kwargs):
        user = self.create_user(first_name, last_name, password, **extra_kwargs)

        user.is_superuser = True
        user.save(using=self._db)
        return user