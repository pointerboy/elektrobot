# Elektrobot - Luka Trbović

from requests import Session
from bs4 import BeautifulSoup as bs

class Sajt():
    def __init__(self, username, password):

        print("Sajt:: Logovanje kao korsinik")

        with Session() as s:
            login_url = 'http://37.0.71.50/ets/login/index.php'
            homepage_url = 'http://37.0.71.50/ets/my/'

            site = s.get(login_url)
            bs_content = bs(site.content, "html.parser")
            login_data = {"username":username, "password":password}
            s.post(login_url, login_data)
            home_page = s.get(homepage_url)
        
            print(home_page.content)
