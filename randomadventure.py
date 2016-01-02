#!/usr/bin/python
# -*- coding: utf-8 -*-
import webbrowser
import urllib2
from bs4 import BeautifulSoup
from randomdotorg import RandomDotOrg

random = RandomDotOrg('RandomAdventure')

print ""


def randomAdventure():
    # Vælg tilfældig sæson mellem 1 og 7
    season = random.randint(1, 7)

    # Der er forskellige antal episoder i hver sæson
    if season <= 4:
        maxepisode = 26
    elif season == 5:
        maxepisode = 52
    elif season == 6:
        maxepisode = 43
    elif season == 7:
        maxepisode = 13
    else:
        print "Der er noget helt galt."

    # Vælg tilfældig episode
    episode = random.randint(1, maxepisode)


    # Lav url
    url = "http://watchseries.lt/episode/Adventure-Time-with-Finn-and-Jake_s" + str(season) + "_e" + str(
        episode) + ".html"

    # Print info
    print "Sæson " + str(season) + " episode " + str(episode) + " valgt."
    return url


def link1():  # Funktion der vælger tilfældigt streaminglink
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    response = opener.open(randomAdventure())
    html = response.read()
    soup = BeautifulSoup(html, "lxml")
    mylist = []
    for a in soup.find_all('a', href=True, class_="buttonlink"):
        # print a['href']
        mylist.extend([a['href']])
    mylist.remove(mylist[0])
    streamLink = "http://watchseries.lt" + random.choice(mylist)
    return streamLink


def link2():  # Funktion der åbner den faktiske streamingside
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    response = opener.open(link1())
    html = response.read()
    myList2 = []
    soup = BeautifulSoup(html, "lxml")
    #Det her er fucking latterligt.
    for a in soup.find_all('a', href=True, class_="myButton"):
        myList2.extend([a['href']])
    return myList2[0]


finalLink = link2()
print "Åbner streaming link: " + finalLink
print  ""
webbrowser.open(finalLink, new=0, autoraise=True)
