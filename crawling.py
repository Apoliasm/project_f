#about text crawling
#mining a article data and processing data
#텍스트 수집 -> 전처리 -> 분석 -> 시각화


from keyword import kwlist
from bs4 import BeautifulSoup
import requests
import pyupbit
import pandas as pd
from matplotlib import pyplot as plt , gridspec
import mplfinance
import numpy
from pytrends.request import TrendReq  #using unofficial api found in github
from pytrends.dailydata import get_daily_data
#There are two module that read url, urllib.request and requests 
#requests get url to dict type, request get url to binary type
#requests is more frequently used


#1. news crawling
def crawling(url):
    open_url = requests.get(url)   #first open url with requsets.get
    open_url.encoding='EUC-KR'   # to show 한글 set variable of request.get -> request.get.encoding = 'EUC-KR'

    soup = BeautifulSoup(open_url.text,features='html.parser')  #second analyze opened html
    articlelist = soup.find_all(name='dl',attrs='article_list') #third find all of tag named specific name
    # 4 factor of html :1.element : all factors in html(title,tag...)  2.tag: made with <p> </p> 
    #3.attribute : set specific command in tag EX) <a href = "www..."> ->href = attribute, 
    #<tag attribute = argument>
    # 4.argument(변수) :  value of attriubte, use with '' or ""
    
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
#3.pytrends to use google trend data
def pytrends():
    return TrendReq()

#3-1
def find_related_keyword(key):
    #1.build class TrendReq()
    #2.set keyword to find with list
    #3.build_payload
    #4.get value with several methods
    #build model
    
    pytrends = TrendReq()
    #provide your search terms
    kw_list = key
    pytrends.build_payload(kw_list)
    #payload = necessary data to use except other peripheral data(peripheral = 부수적인,지엽적인)
    
    #get related queries
    related_queries = pytrends.related_queries()
    related_queries.values()

    #build lists dataframes

    top = list(related_queries.values())[0]['top']
    rising = list(related_queries.values())[0]['rising']

    #convert lists to dataframes

    dftop = pd.DataFrame(top)
    dfrising = pd.DataFrame(rising)

    #join two data frames
    joindfs = [dftop, dfrising]
    allqueries = pd.concat(joindfs, axis=1)

    #function to change duplicates

    cols=pd.Series(allqueries.columns)
    for dup in allqueries.columns[allqueries.columns.duplicated(keep=False)]: 
        cols[allqueries.columns.get_loc(dup)] = ([dup + '.' + str(d_idx) 
                                        if d_idx != 0 
                                        else dup 
                                        for d_idx in range(allqueries.columns.get_loc(dup).sum())]
                                        )
    allqueries.columns=cols

    #rename to proper names

    allqueries.rename({'query': 'top query', 'value': 'top query value', 'query.1': 'related query', 'value.1': 'related query value'}, axis=1, inplace=True) 

    #check your dataset
    print(allqueries.head(50))

    #save to csv
    allqueries.to_csv('allqueries.csv')
    
#find and train related data

def check_news():        
    url_crypto = "https://www.mk.co.kr/news/crypto-currency/"
    url_econo = 'https://www.mk.co.kr/news/economy/'
    url_global_finance = 'https://www.mk.co.kr/news/world/global-finance/'
    url_stock = 'https://www.mk.co.kr/news/stock/'
    inputed = input("crypto = Type 'c,economy = Type 'e',global finance = Type 'gf',stock ='st',exit = Type 'x ")
    while (inputed != 'x'):
        if inputed == 'c':
            crawling(url_crypto)
            inputed = input("crypto = Type 'c,economy = Type 'e',global finance = Type 'gf',stock ='st',exit = Type 'x ")
        elif inputed == 'e':
            crawling(url_econo)
            inputed = input("crypto = Type 'c,economy = Type 'e',global finance = Type 'gf',stock ='st',exit = Type 'x ")
        elif inputed == 'gf':
            crawling(url_global_finance)
            inputed = input("crypto = Type 'c,economy = Type 'e',global finance = Type 'gf',stock ='st',exit = Type 'x ")
        elif inputed == 'st':
            crawling(url_stock)
            inputed = input("crypto = Type 'c,economy = Type 'e',global finance = Type 'gf',stock ='st',exit = Type 'x ")
                
        elif inputed == 'x':
            break
