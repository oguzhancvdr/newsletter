import requests
from pprint import pprint

# test registiration is work or not on behalf of client side
def client():
    credentials = {
      'username': 'rest_test_user',
      'email': 'test@test.com',
      'password1': 'testing123.',
      'password2': 'testing123.',
    }
    
    # burada django-rest-auth'dan faydalandık '/api/rest-auth/registration/'
    response = requests.post(url='http://127.0.0.1:8000/api/rest-auth/registration/', data=credentials,)
    print('Status code: ', response.status_code)
    response_data = response.json()
    pprint(response_data)


if __name__ == '__main__':
    client()