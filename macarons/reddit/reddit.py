import urllib.request, urllib.parse, urllib.error
import time # This is for checking on the transparency report
from datetime import date # Get the date
import json
from bs4 import BeautifulSoup # Huzzah to BeautifulSoup cuteness!

#########################
#  Playing with urllib  #
#########################
# transparency_report_2016=urllib.request.urlopen('https://www.reddit.com/wiki/transparency/2016').read()
# transparency_report_2015=urllib.request.urlopen('https://www.reddit.com/wiki/transparency/2015').read()
# Turns out you can't do multiple requests like this
# 
transparency_report_2014=urllib.request.urlopen('https://www.reddit.com/wiki/transparency/2014').read()

################################
#  Playing with BeautifulSoup  #
################################
# soup_2016=BeautifulSoup(transparency_report_2016,'html.parser')
# soup_2015=BeautifulSoup(transparency_report_2015,'html.parser')
# soup_2014=BeautifulSoup(transparency_report_2015,'html.parser')
# Turns out you can't do multiple requests like this
# 
soup=BeautifulSoup(transparency_report_2014,'html.parser')
# soup=BeautifulSoup(open("reddit_2014.html"),'html.parser')

print(soup.prettify().encode('utf-8'))