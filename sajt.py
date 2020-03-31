# Elektrobot - Luka Trbović

from requests import Session
from bs4 import BeautifulSoup as bs
from lxml import html

class SajtPredmeti():
    url = 'http://37.0.71.50/ets/course/view.php?id='
    informatika = url + str(287)

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
        home_page = Sajt.s.get(SajtPredmeti.informatika)
        
        print(home_page)

    def ListajIteme(self, id_predmeta: int):
        stranica_url = SajtPredmeti.url+str(id_predmeta)

        stranica = Sajt.s.get(stranica_url)
        lista = html.fromstring(stranica.content)

        test = lista.xpath('//span[@class="instancename"]/text()')
        print(test)
