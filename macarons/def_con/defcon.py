import urllib
import time # This is for checking on the transparency report
import datetime # Also for the transparency report
import json
from bs4 import BeautifulSoup # Huzzah to BeautifulSoup cuteness!

#########################
#  Playing with urllib  #
#########################
# Lets use the urllib3 library to get the report!
# https://www.defcon.org/html/links/dc-transparency.html
#
transparency_report=urllib.urlopen('https://www.defcon.org/html/links/dc-transparency.html').read()

################################
#  Playing with BeautifulSoup  #
################################
# With the grabbed link lets make it into soup!
#
soup=BeautifulSoup(transparency_report,'html.parser')
#
# Results should print out: <class 'bs4.BeautifulSoup'>
# print type(soup)

# This is the 31 July 2017 web page
# Eventually I'll make this dynamic with urllib3
#
# soup=BeautifulSoup(open("def_con_31_07_2017.html"),'html.parser')

# BeautifulSoup will make this look really gorgeous in the terminal!
# This works huzzah!
# I had to add in .encode('utf-8') to stop an ascii error
#
# print(soup.prettify().encode('utf-8'))

# Find the full transparency report which is wrapped in <code> tags with BeautifulSoup
report=soup.find_all('code')

# There may be more <code> elements on the page so lets find out!
# Aw golly this works too!
#
# for code in report:
#     print code

# Hopefully pull stuff into macarons?
for macarons in report:
    # macarons is printing correctly
    print macarons
    #
    # This is currently not working
    # with open("defcon.json", "w") as writeJSON:
    #     json.dump(macarons, writeJSON)

#######################
#  Playing with time  #
#######################
