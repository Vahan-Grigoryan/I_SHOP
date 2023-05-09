from django.contrib.auth.base_user import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, password, **extra_kwargs):
        if not all((first_name, last_name, password)):
            raise ValueError('Provide first_name, last_name, password,')

        user = self.model(
            first_name = first_name,
            last_name = last_name,
            email = self.normalize_email(extra_kwargs.pop('email')),
            **extra_kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, password, **extra_kwargs):
        user = self.create_user(first_name, last_name, password, **extra_kwargs)

        user.is_superuser = True
        user.save(using=self._db)
        return user