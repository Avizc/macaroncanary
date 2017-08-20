import urllib.request, urllib.parse, urllib.error
import time # This is for checking on the transparency report
from datetime import date # Get the date
import json
from bs4 import BeautifulSoup # Huzzah to BeautifulSoup cuteness!

#########################
#  Playing with urllib  #
#########################
# Lets use the urllib3 library to get the report!
# https://www.defcon.org/html/links/dc-transparency.html
#
transparency_report=urllib.request.urlopen('https://www.defcon.org/html/links/dc-transparency.html').read()

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
#     print(code)

# Hopefully pull stuff into macarons?
for macarons in report:
    # macarons is printing correctly
    print("##### BELOW IS MACARONS #####",macarons,"##### THE ABOVE IS MACARONS #####")
    #
    # This is working sending to defcon.txt
    # Out of scope for this week to do JSON
    # Will work on it in the future!
    with open("defcon.txt", "w") as writeTXT:
        print(macarons,file=writeTXT)

#######################
#  Playing with time  #
#######################
# Lets print today's date
#
todays_date=date.today()
print("Today's date!",todays_date)
#
# Lets print a future date
#
# october=date(todays_date.year,10,1)
# print "This is for 1 October",october
#
# Test out dates
#
test_date=date(todays_date.year,3,5)
print("Print 5 March 2017",test_date)
another_date=date(todays_date.year,5,7)
print("Print 7 May 2017",another_date)
same_date=date(todays_date.year,3,5)
print("Print 5 March 2017",same_date)
#
if test_date==another_date:
    print("This isn't working, they should be different days")
else:
    print("This is working, they are different days")
#
# Cool that worked!
#
if test_date!=same_date:
    print("This isn't working, they are the same date")
else:
    print("This is working, they are the same date")
#
# Cool that worked, too!
#
today=date.today()
print("This is today's date, today!", today)
today_maybe=(today.year,8,18)
print("This should be today's date", today_maybe)
macarons=date(today.year,10,1) # Next date-ish it should update
if today_maybe==today:
    today_maybe=today_maybe.replace(month=today.month+2)
# print("This should be two months ahead of today",today_maybe)
# if macarons==today:
#     macarons=macarons.replace(month=today.month+2)
# print macarons