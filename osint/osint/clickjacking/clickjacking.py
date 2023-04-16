import requests


def check_clickjacking(url):
    try:
        response = requests.get(url)
        if 'X-Frame-Options' not in response.headers:
            print(f'Clickjacking осалдығы анықталды: {url}')
            print('Осалдық пайызы: 100%')
            return 1
        else:
            print(f'Clickjacking осалдығы анықталмады {url}')
            print('Осалдық пайызы: 0%')
            return 0
    except requests.exceptions.RequestException as e:
        print(f'Clickjacking осалдығын тексеру кезінде қате орын алды {url}')
        print(f'Қате туралы хабар: {e}')
