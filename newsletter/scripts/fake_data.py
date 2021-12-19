import os
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsletter.settings')

import django
django.setup()
# Modellerimize ve django içeriklerine erişim için yukardaki adımları yapmamız lazım.
# ! sıralama çok önemli
from django.contrib.auth.models import User
from faker import Faker

def set_user():
    fake = Faker(['en_US'])

    f_name = fake.first_name()
    l_name = fake.last_name()
    u_name = f"{f_name.lower()}_{l_name.lower()}"
    email = f"{u_name.lower()}@{fake.domain_name()}"
    print(f_name, l_name, email)

    user_check = User.objects.filter(username=u_name)

    while user_check.exists():
        u_name = u_name + str(random.randrange(1,99))
        user_check = User.objects.filter(username=u_name)


    user = User(
      username=u_name,
      first_name=f_name,
      last_name=l_name,
      email=email,
      is_staff= fake.boolean(chance_of_getting_true=75),
    )

    user.set_password('testing123.')
    user.save()