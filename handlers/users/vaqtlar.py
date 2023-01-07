import requests
from bs4 import BeautifulSoup as BS

def bugun(viloyat):
    link = f"https://namozvaqti.uz/shahar/{viloyat}"
    r = requests.get(link).text
    soup = BS(r,"html.parser")
    bugun = soup.select(".vil")[0].text
    return bugun

def hozirgi(viloyat):
    link = f"https://namozvaqti.uz/shahar/{viloyat}"
    r = requests.get(link).text
    soup = BS(r,"html.parser")
    bugun = soup.select(".current_time")[0].text
    return bugun

def bomdod(viloyat):
    link = f"https://namozvaqti.uz/shahar/{viloyat}"
    r = requests.get(link).text
    soup = BS(r,"html.parser")
    bugun = soup.select(".time")[0].text
    return bugun
def quyosh(viloyat):
    link = f"https://namozvaqti.uz/shahar/{viloyat}"
    r = requests.get(link).text
    soup = BS(r,"html.parser")
    bugun = soup.select(".time")[1].text
    return bugun

def peshin(viloyat):
    link = f"https://namozvaqti.uz/shahar/{viloyat}"
    r = requests.get(link).text
    soup = BS(r,"html.parser")
    bugun = soup.select(".time")[2].text
    return bugun

def asr(viloyat):
    link = f"https://namozvaqti.uz/shahar/{viloyat}"
    r = requests.get(link).text
    soup = BS(r,"html.parser")
    bugun = soup.select(".time")[3].text
    return bugun

def shom(viloyat):
    link = f"https://namozvaqti.uz/shahar/{viloyat}"
    r = requests.get(link).text
    soup = BS(r,"html.parser")
    bugun = soup.select(".time")[4].text
    return bugun

def xufton(viloyat):
    link = f"https://namozvaqti.uz/shahar/{viloyat}"
    r = requests.get(link).text
    soup = BS(r,"html.parser")
    bugun = soup.select(".time")[5].text
    return bugun