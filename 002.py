#data training file
from bs4 import BeautifulSoup
import requests
import pyupbit
import pandas as pd
from matplotlib import pyplot as plt , gridspec
import mplfinance
import numpy
from pytrends.request import TrendReq  #using unofficial api found in github
from pytrends.dailydata import get_daily_data
from . import crawling



#There are two module that read url, urllib.request and requests 
#requests get url to dict type, request get url to binary type
#requests is more frequently used

def train_keyword