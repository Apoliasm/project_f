from keyword import kwlist
from bs4 import BeautifulSoup
import requests
import pyupbit
import pandas as pd
from matplotlib import pyplot as plt , gridspec
import mplfinance
import numpy
from pytrends.request import TrendReq
import os
import sys


def main ():
    
    menu = input("type menu : type 1: check news about topic , type 2: check releted keywords, type 0:exit")
    while(menu != '0'):
        if menu == '1' :
            keylist = list()
            keyword = input("type keyword you want to find related things : ")
            keylist.append(keyword)
            crawling.find_related_keyword(key=keylist)
            menu = input("type menu : type 1: check news about topic , type 2: check releted keywords,")
        elif menu == '2' :
            crawling.check_news()
            menu = input("type menu : type 1: check news about topic , type 2: check releted keywords,")

if __name__ == '__main__':
    import crawling
    main()

    