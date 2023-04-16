import requests
from urllib.parse import urljoin


def check_sql_injection(url):
    try:
        payload = "1' OR '1'='1"
        response = requests.get(urljoin(url, '?id=' + payload))
        if 'error' in response.text:
            print(f'SQL инъекциясының осалдығы анықталды {url}')
            print('Осалдық пайызы: 100%')
            return 1
        else:
            print(f'SQL инъекциясының осалдығы анықталмады {url}')
            print('Осалдық пайызы: 0%')
            return 1
    except requests.exceptions.RequestException as e:
        print(f'SQL инъекциясының осалдығын тексеру кезінде қате орын алды {url}')
        print(f'Қате туралы хабар: {e}')

