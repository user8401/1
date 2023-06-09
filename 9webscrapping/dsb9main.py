import requests
from bs4 import BeautifulSoup
HEADERS = (
    { 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0)',
      'Accept-Language': 'en-US,en;'
    }
)
def getdata(url):
    r = requests.get(url, headers=HEADERS)
    return r.text
def html_code(url):
    htmldata = getdata(url)
    soup = BeautifulSoup(htmldata, 'html.parser')
    return (soup)
url = '''https://www.amazon.in/Fastrack-Limitless-Biggest-SingleSync-Watchfaces/dp/B0BZ8T21V4?ref_=Oct_DLandingS_D_24acc1f0_0&th=1'''
soup = html_code(url)
def cus_data(soup):
    data_str = ""
    cus_list = []
    for item in soup.find_all("span", class_="a-profile-name"):
        data_str = data_str + item.get_text()
        cus_list.append(data_str)
        data_str = ""
    return cus_list
cus_res = cus_data(soup)
print(cus_res)
def cus_rev(soup):
    data_str = ""
    for item in soup.find_all("div", class_="a-section review aok-relative"):
        data_str = data_str + item.get_text()
    result = data_str.split("\n")
    return (result)
rev_data = cus_rev(soup)
rev_result = []
for i in rev_data:
    if i is "":
        pass
    else:
        rev_result.append(i)
import numpy as np
rev_result_fetch = rev_result[0:10]
cus_res_fetch = cus_res[0:10]
import pandas as pd
data = {'Name': cus_res_fetch,'review': rev_result_fetch}
df = pd.DataFrame(data)
df.to_csv('C:/Users/prath/Downloads/review.csv');
import pandas as pd
df=pd.read_csv("C:/Users/prath/Downloads/review.csv");
print(df.head());
data = df.to_dict(orient="records");
print(data);