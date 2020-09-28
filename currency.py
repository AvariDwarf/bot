import requests
from bs4 import BeautifulSoup

class Currency:
    RUB_page = 'https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%3A1584716087546&source=hp&ei=N9l0XtDXHs716QTcuaXoAg&q=доллар+к+рублю&oq=доллар+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4'
    BYN_page = 'https://www.google.com/search?sxsrf=ALeKk00QXZ8tt3U9X0QR7a2Q8o63Ijm6-w%3A1601238400347&ei=gPVwX9DZFMrHrgSbmozICw&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D0%B1%D0%B5%D0%BB%D0%BE%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%BC%D1%83+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+&gs_lcp=CgZwc3ktYWIQARgEMgQIIxAnMgQIIxAnMgQIIxAnMgcIABAUEIcCMgIIADICCAAyAggAMgIIADICCAAyBAgAEEM6BAgAEEc6BAgAEApQ3IsBWOSPAWDbpgFoAHACeACAAWeIAYUDkgEDMi4ymAEAoAEBqgEHZ3dzLXdpesgBCMABAQ&sclient=psy-ab'
    EUR_page = 'https://www.google.com/search?sxsrf=ALeKk01un43gAr9aPBcEe-hIJE3xZkMXuQ%3A1601238375282&ei=Z_VwX5bzEO_FrgSR8KWwBA&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D0%B5%D0%B2%D1%80%D0%BE&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D0%B5%D0%B2%D1%80&gs_lcp=CgZwc3ktYWIQARgAMgoIABCxAxBGEIICMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAOgQIABBHOgcIABAUEIcCOgQIABANOgQIIxAnOgUIABCxAzoPCAAQsQMQFBCHAhBGEIICOgQIABAKUPWQAVi9qgFgvbgBaANwAngAgAF0iAGwB5IBAzIuN5gBAKABAaoBB2d3cy13aXrIAQjAAQE&sclient=psy-ab'
    BTC_page = 'https://www.google.com/search?sxsrf=ALeKk00VsBs0FHjaLG8fGKmOuboGiNkQhQ%3A1601238360855&ei=WPVwX4vnM4yxrgSu_5TgBg&q=доллар+к+биткоину&oq=доллар+к+биткоину&gs_lcp=CgZwc3ktYWIQAzIHCAAQRhCCAjICCAAyAggAMgYIABAWEB46BAgAEEc6BAgjECc6CQgjECcQRhCCAjoECAAQCjoHCAAQFBCHAjoFCAAQsQM6BggAEA0QHjoICAAQFhAKEB5QvhNYxWNgl2VoA3ACeACAAYEBiAHVDZIBBDQuMTKYAQCgAQGqAQdnd3Mtd2l6yAEIwAEB&sclient=psy-ab&ved=0ahUKEwiL88vdlYrsAhWMmIsKHa4_BWwQ4dUDCA0&uact=5'

    HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36', 'accept-language': 'ru,en;q=0.9'}

    RUB = 0
    BYN = 0
    EUR = 0
    BTC = 0
    RSF = 0

    TIME = ''

    def __init__(self):
      self.RUB = float(str(self.get_currency()[0]).replace(',' , '.'))
      self.BYN = float(str(self.get_currency()[1]).replace(',' , '.'))
      self.EUR = float(str(self.get_currency()[2]).replace(',' , '.'))
      self.BTC = float(str(self.get_currency()[3]).replace(',' , '.'))

      self.TIME = self.get_currency()[4]

      #self.RSF = float()

    def get_currency(self):
      pages = [requests.get(self.RUB_page, headers=self.HEADERS), requests.get(self.BYN_page, headers=self.HEADERS), requests.get(self.EUR_page, headers=self.HEADERS), requests.get(self.BTC_page, headers=self.HEADERS)]
      soup = []
      convert = []

        # for p in pages:
        #     soup.append(BeautifulSoup(p.content, 'html.parser'))

      for p in pages:
        soup.append(BeautifulSoup(p.text, 'html.parser'))

      for s in soup:
        convert.append(s.find('span', class_='DFlfde SwHCTb').text)

      convert.append(soup[0].find('div', class_='hqAUc').find('span').text)
      return convert

#currency = Currency()
