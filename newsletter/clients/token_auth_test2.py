import requests
from pprint import pprint


def client():

    token = 'Token c70dabea9adaed6b734013eb26c617d899e2cd4b'
    headers = {
      'Authorization': token,
    }
    response = requests.get(url='http://127.0.0.1:8000/api/user_profiles/', headers=headers,)
    print('Status code: ', response.status_code)
    response_data = response.json()
    pprint(response_data)


# burda direk tokensız istek attığımızda döncek cevabı test ediyoruz
# terminalden py bu_dosya'yı run ettiğimizde ilgili print cevaplarını alıyoruz
# bundan sonra token ekleyerek deneyelim
if __name__ == '__main__':
    client()