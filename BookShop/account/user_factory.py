import factory
from django.contrib.auth.hashers import make_password


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'account.User'

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    password = make_password(str(factory.Faker('password')))
    is_active = True
    is_staff = False
    is_superuser = False