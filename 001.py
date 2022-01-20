#about text crawling
#mining a article data and processing data
#텍스트 수집 -> 전처리 -> 분석 -> 시각화


from bs4 import BeautifulSoup
import requests
import pyupbit
import pandas as pd
from matplotlib import pyplot as plt , gridspec
import mplfinance
import numpy
#There are two module that read url, urllib.request and requests 
#requests get url to dict type, request get url to binary type
#requests is more frequently used

#1. news crawling
def crawling(url):
    open_url = requests.get(url)
    open_url.encoding='EUC-KR'   # to show 한글 set variable of request.get -> request.get.encoding = 'EUC-KR'

    soup = BeautifulSoup(open_url.text,features='html.parser')
    articlelist = soup.find_all(name='dl',attrs='article_list')
    for index,things in enumerate(articlelist) :
        articlelist[index] = articlelist[index].text
        print(articlelist[index])
    #class BeautifulSoup
#2. crypto chart
def chart_crypto ():
    price = pyupbit.get_current_price("KRW-BTC")
    ohlcv = pd.DataFrame(pyupbit.get_ohlcv("KRW-MANA",count=200,to='20211129'))
    print("current price = ",price)
    ohlcv.insert(len(ohlcv.columns),'fluctuation',0)  #dataframe.insert : insert new column
    ohlcv.insert(len(ohlcv.columns),'percentage',0)
    for open,close,fluc in zip(ohlcv['open'],ohlcv['close'],range(200)) : 
        ohlcv['fluctuation'][fluc] = close-open
        ohlcv['percentage'][fluc] = (close-open)/open*100
    
    #sorting dictionary: using sorted() / dict.items() -> alter dict to tuple/ operator.itemgetter(0 or 1) 0 is key,1 is value
    sorted = ohlcv.sort_values('percentage',)
    print(ohlcv,'\n')
    print("low top 3 : \n",sorted.head(20))
    print("high top 3: \n",sorted.tail(20))


chart_crypto()
#main
url_crypto = "https://www.mk.co.kr/news/crypto-currency/"
url_econo = 'https://www.mk.co.kr/news/economy/'
url_global_finance = 'https://www.mk.co.kr/news/world/global-finance/'
inputed = input("crypto = Type 'c,economy = Type 'e',global finance = Type 'gf',exit = Type 'x ")
while (inputed != 'x'):
    if inputed == 'c':
        crawling(url_crypto)
        inputed = input("crypto = Type 'c,economy = Type 'e',global finance = Type 'gf',exit = Type 'x ")
    elif inputed == 'e':
        crawling(url_econo)
        inputed = input("crypto = Type 'c,economy = Type 'e',global finance = Type 'gf',exit = Type 'x ")
    elif inputed == 'gf':
        crawling(url_global_finance)
        inputed = input("crypto = Type 'c,economy = Type 'e',global finance = Type 'gf',exit = Type 'x ")
    elif inputed == 'x':
        break

