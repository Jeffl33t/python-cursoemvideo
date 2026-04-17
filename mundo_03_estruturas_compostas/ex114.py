import urllib.request
import urllib.error


def consulta_site(url):
    try:
        site = urllib.request.urlopen(url)
    except urllib.error.URLError:
        print(f'\033[31mO site {url} não está acessível no momento.\033[m')
    else:
        print(f'\033[32mConsegui acessar o site {url} com sucesso!\033[m')


consulta_site('http://google.com.br')