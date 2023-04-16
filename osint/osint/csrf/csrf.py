import requests


def check_csrf(url):
    try:
        payload = {'username': 'attacker', 'password': 'password', 'csrf_token': 'fake_token'}
        response = requests.post(url, data=payload)
        if 'Invalid CSRF Token' in response.text:
            print(f'CSRF осалдығы анықталды{url}')
            print('Осалдық пайызы: 100%')
            return 1
        else:
            print(f'CSRF осалдығы анықталмады {url}')
            print('Осалдық пайызы: 0%')
            return 0
    except requests.exceptions.RequestException as e:
        print(f'CSRF осалдығын тексеру кезінде қате орын алды {url}')
        print(f'Қате туралы хабар: {e}')
