import urllib.request, urllib.parse, urllib.error
import time # This is for checking on the transparency report
from datetime import date # Get the date
import json
from bs4 import BeautifulSoup # Huzzah to BeautifulSoup cuteness!

#########################
#  Playing with urllib  #
#########################
transparency_report=urllib.request.urlopen('https://riseup.net/about-us/canary/canary-statement-signed.txt').read()

################################
#  Playing with BeautifulSoup  #
################################
soup=BeautifulSoup(transparency_report,'lxml')
print(soup.prettify())