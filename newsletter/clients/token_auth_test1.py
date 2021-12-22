import requests
from pprint import pprint


def client():
    credentials = {
      'username': 'aaron_harrison',
      'password': 'testing123.'
    }
    # burada django-rest-auth'dan faydalandık '/api/rest-auth/login/'
    response = requests.post(url='http://127.0.0.1:8000/api/rest-auth/login/', data=credentials,)
    print('Status code: ', response.status_code)
    response_data = response.json()
    pprint(response_data)


# ben bu dosyayı terminalde çağırdığıumda çalışacak fonks tanımladım
# burda client olarak login olmayı simülasyon ediyoruz 
if __name__ == '__main__':
    client()


# after run this file token was tkaen in terminal
# and just check this user's token in admin page as well
# {'key': 'c70dabea9adaed6b734013eb26c617d899e2cd4b'}