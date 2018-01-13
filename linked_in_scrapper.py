from bs4 import BeautifulSoup
import requests
import json

class Linked_in_scraper:

    def scrape_profile_div(self, user_profile_url):

# Start session
        client = requests.Session()

        HOMEPAGE_URL = 'https://www.linkedin.com/uas/login'
        LOGIN_URL = 'https://www.linkedin.com/uas/login-submit'

# go to login page and get tokens
        html = client.get(HOMEPAGE_URL).content
        soup_login = BeautifulSoup(html, 'html.parser')
        csrf = soup_login.find(id="loginCsrfParam-login")['value']

# prepare header for POST request
        login_information = {
            'session_key': 'redleafpro@gmail.com',
            'session_password': 'asasas12',
            'loginCsrfParam': csrf,
        }

# login to linkedIn
        client.post(LOGIN_URL, data=login_information)

# get profile page
        profile_page = client.get(user_profile_url)

        soup_profile = BeautifulSoup(profile_page.content, 'html.parser')

        # html = soup_profile.prettify("utf-8")

        with open("linkedin.html", "wb") as file:
            file.write(html)

#  extract info from profile
        user_profile = {}
        name = soup_profile.find_all('code')
        # print(soup.title.string)
        print (name[26].text)
        m=name[26].text
        n = json.dumps(26)


    def scrape_one_profile(self, profile_url):
        return self.scrape_profile_div(profile_url)

    def __init__(self, profile_name):
        self.profile_name = profile_name
