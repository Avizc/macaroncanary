from bs4 import BeautifulSoup # Huzzah to BeautifulSoup cuteness!
# Eventually I'll be using urllib3 but not right now!
# import urllib3

# This is the 31 July 2017 web page
# Eventually I'll make this dynamic with urllib3
soup=BeautifulSoup(open("def_con_31_07_2017.html"),'html.parser')

# BeautifulSoup will make this look really gorgeous in the terminal!
# I had to add in .encode('utf-8') to stop an ascii error
print(soup.prettify().encode('utf-8'))