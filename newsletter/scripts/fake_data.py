import os
import random

from rest_framework import serializers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsletter.settings')

import django
django.setup()
# Modellerimize ve django içeriklerine erişim için yukardaki adımları yapmamız lazım.
# ! sıralama çok önemli
from django.contrib.auth.models import User
from faker import Faker
import requests

fake = Faker(['en_US'])
def set_user():

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

from pprint import pprint
from books.api.serializers import BookSerializer


def add_book(subject):
    url = 'http://openlibrary.org/search.json'
    payload = {'q': subject}
    response = requests.get(url, params=payload)

    if response.status_code != 200:
        print('Opps!', response.status_code)
        return

    jsn = response.json()
    books = jsn.get('docs')

    for book in books:
      book_name = book.get('title')
      data = dict(
        name = book_name,
        author = book.get('author_name')[0],
        description = book.get('title_suggest'),
        published_at = fake.date_time_between(start_date="-10y", end_date="now", tzinfo=None),
      )
      # çekilen fake datayı db'ye serializer aracalığıyla kaydediyoruz
      serializer = BookSerializer(data=data)
      if serializer.is_valid():
        serializer.save()
        print(f'Named as {book_name} book was saved')
      else:
        continue
      