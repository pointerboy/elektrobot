# Elektrobot - Luka Trbović

from requests import Session
from bs4 import BeautifulSoup as bs
from lxml import html

import json 

class SajtPredmeti():
    url = 'http://37.0.71.50/ets/course/view.php?id='
    lista_predmeta = [("Informatika",287,
                      "Matematika", 333)]

class Sajt():
    s = Session()
    def __init__(self, username, password):

        print("Sajt:: Logovanje kao korsinik")
        login_url = 'http://37.0.71.50/ets/login/index.php'
        homepage_url = 'http://37.0.71.50/ets/my/'

        site = Sajt.s.get(login_url)
        bs_content = bs(site.content, "html.parser")
        login_data = {"username":username, "password":password}
        Sajt.s.post(login_url, login_data)

    def KolektujIteme(self):
        with open('predmeti.json') as f:
            data = json.load(f)

            for i in data['predmeti']:
                print("Sajt:: Kolektovanje predmeta ", i['ime'])

                rezultat = Sajt.VratiItem(self, i['index'])
                filed = open(i['ime']+".txt", 'w')
                filed.write(rezultat)
                f.close()
                print("Sajt:: i['ime'] ", "je kolektovan.")
         
    def VratiItem(self, id_predmeta: int):
        stranica_url = SajtPredmeti.url+str(id_predmeta)

        stranica = Sajt.s.get(stranica_url)
        lista = html.fromstring(stranica.content)

        kontent= lista.xpath('//span[@class="instancename"]/text()')
        return kontent
