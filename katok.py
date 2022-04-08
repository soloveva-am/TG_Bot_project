import requests
from bs4 import BeautifulSoup
def public_skating():
    url = 'https://dol-sport.ru/page/massovoe-katanie'
    r = requests.get(url)
    content = BeautifulSoup(r.text, 'html.parser').text.replace('\xa0', ' ').replace('\u200b', ' ').replace('\n\n', '\n')
    content = content[content.find('Массовое катание'):content.find('Хоккейное катание')]
    print(content)
    return content

content = public_skating()
list_skat = content.split("\n")
list_skat = list_skat[1:len(list_skat)-1]

def dict_skating(list_skat):
    skat = {}
    for a in list_skat:
        b = a.find(":")
        c = a[:b]
        d = a[b+2:]
        skat[c] = d
    return skat
print(dict_skating(list_skat))

