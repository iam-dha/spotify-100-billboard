from bs4 import BeautifulSoup
import requests
from requests import Request, HTTPError

WEB = f"https://www.billboard.com/charts/hot-100/"


class Crawler:
    def __init__(self):
        self.header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
        self.data = []

    def crawl(self, date_to_crawl):
        path = f"{WEB}{date_to_crawl}/"
        try:
            response =  requests.get(url= path, headers= self.header)
        except HTTPError:
            print(f"Exception {response.status_code}")
        else:
            soup = BeautifulSoup(markup= response.text, features= 'html.parser')
        soup = soup.find(name = "div", class_ = "chart-results-list // lrv-u-padding-t-150 lrv-u-padding-t-050@mobile-max")
        data = soup.find_all(name = "div", class_="o-chart-results-list-row-container")
        for line in data:
            self.data.append(line.ul.find(name="h3", id="title-of-a-story").getText().strip())

    def get_data(self):
        return self.data



