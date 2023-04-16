import requests


def check_info(url):
    try:
        list_of_adres = ['sitemap.xml', 'robots.txt', 'info.php', 'requirments.txt']
        infomass = []
        for i in range(0, len(list_of_adres)):
            response = requests.get(url + list_of_adres[i])
            if (response):
                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print("check_info(" + url + ")" + "[" + list_of_adres[i] + "]")
                print(response.text)
                infomass.append({"name": list_of_adres[i], "text": response.text})
        return infomass
    except Exception as e:
        print(f'Қате орын алды: {e}')
