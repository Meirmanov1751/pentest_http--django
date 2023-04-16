import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup


def check_xss(url):
    try:
        payload = '<script>alert("XSS")</script>'
        response = requests.get(urljoin(url, payload))
        soup = BeautifulSoup(response.text, 'html.parser')
        if payload in soup.text:
            print(f'XSS осалдығы анықталды {url}')
            print('Осалдық пайызы: 100%')
            return 1
        else:
            print(f'XSS осалдықтары табылмады {url}')
            print('Осалдық пайызы: 0%')
            return 0
    except requests.exceptions.RequestException as e:
        print(f'XSS осалдығын тексеру кезінде қате орын алды {url}')
        print(f'Қате туралы хабар: {e}')

