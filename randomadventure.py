#!/usr/bin/python
# -*- coding: utf-8 -*-

# SOMEONE PLEASE FORK THIS! I CANT STAND LOOKING AT IT! SO. BADLY. CODED. *crying*


import os
import webbrowser
import json
import urllib2
from urllib2 import Request, urlopen, URLError
from bs4 import BeautifulSoup
from randomdotorg import RandomDotOrg
import textwrap

random = RandomDotOrg('RandomAdventure')

class bcolors:
    OKBLUE = '\033[94m'
    RED = '\033[31m'
    ENDCOLOR = '\033[0m'
    BOLD = '\033[1m'
    ATBG = '\033[40m'
    ATFG = '\033[33m'
    DIM = '\033[2m'
    UNDERLINE = '\033[4m'



#########INDSTILLINGER#########
preference = "vodlocker"  # Hvilken streamingside vil du helst benytte?
#Muligheder:
"""
allmyvideos, bestreams, beta.vidup, briskfile, cloudtime, cloudzilla, daclips, filecore,
filehoot, filenuke, flashx, gorillavid, happystreams, hdshare, letwatch, mega-vids,
mightyupload, movbux, movdivx, movpod, neodrive, nosvideo, nowvideo, ovfile, promptfile,
putlocker, realvid, sharerepo, sharesix, skyvids, streamcloud, streamin, thefile, thevideo,
uploadc, uploaded, vid, vidbull, videla, video, videostoring, vidlockers, vidspot, vidto,
vidzi, vodlocker, zalaa
"""
##############################


def randomAdventure():  # Funktion der finder et tilfældigt afsnit og dets info vha. Adventure Time API
    print "Getting super random numbers from the internetz. Please wait..."
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'randomAdventure 0.2')]

    # Parse JSON fra webserveren
    response = opener.open("http://adventuretimeapi.com/api/v1/episodes/")
    parsed_json = json.loads(response.read())

    # Tjek hvor mange episoder der findes
    episodeCount = (parsed_json['count'])

    while True:  # Tjek om data fra webserveren indeholder episode og sæson ID (Tjek om det faktisk er en episode)

        # Lav et tilfældigt tal mellem 1 og antallet af episoder
        episode_api = random.randint(1, episodeCount)

        # Hent data om episoden
        response = opener.open("http://adventuretimeapi.com/api/v1/episodes/" + str(episode_api))
        parsed_json = json.loads(response.read())

        # Lav variabler med data
        season = parsed_json['season_id']
        episode = parsed_json['episode_id']
        title = parsed_json['title']
        description = parsed_json['description']

        # Hvis ikke episode variablen indeholder noget, har vi fået en comic eller lign. fra serveren
        if episode is not None:
            break
        elif episode is None:
            print "The Adventure Time API gave us something that wasn\'t an episode. Maybe a comic. Trying again...\n"

    # Sammensæt url med tilfældige tal
    url = "http://www.watchseries.lt/episode/Adventure-Time-with-Finn-and-Jake_s" + str(season) + "_e" + str(
            episode) + ".html"

    # Det her er simpelthen for latterligt og der er 100% en meget smartere måde at gøre det på, men jeg er en fucking idiot.
    # Saml data om episoden i en list
    episodeInfo = []
    episodeInfo.append(str(season))
    episodeInfo.append(str(episode))
    episodeInfo.append(description)
    episodeInfo.append(url)
    episodeInfo.append(title)

    # Return listen med episodedata
    return episodeInfo


def link1():  # Funktion der vælger streaminglink
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]  # Watchseries.lt blokerer underlige user-agents
    # Suk
    episodeinfo2 = randomAdventure()


    try: #Tjek for URLError/HTTPError ved forbindelse til watchseries.lt
        response = opener.open(str(episodeinfo2[3]))

    except URLError as e: #FEJL
        print bcolors.RED
        if hasattr(e, 'reason'):
            print 'Failed to reach the stream indexing server.'
            print 'Reason: ', e.reason
            print bcolors.ENDCOLOR
            quit()
        elif hasattr(e, 'code'):
            print 'The stream indexing server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
            print bcolors.ENDCOLOR
            quit()

    else: #Ingen fejl

        html = response.read()
        soup = BeautifulSoup(html, "lxml")
        mylist = []

        # Benyt foretrukken streamingside
        if preference != "" and soup.find_all('a', href=True, title=preference) != []:

            for a in soup.find_all('a', href=True, title=preference):
                mylist.extend([a['href']])

            # Lav URL med tilfældigt valgt link til foretrukken streamingside
            streamLink = "http://watchseries.lt" + random.choice(mylist)
            episodeinfo2.append(streamLink)

            return episodeinfo2

        else:

            for a in soup.find_all('a', href=True, class_="buttonlink"):
                mylist.extend([a['href']])

            # Første link er en reklame - fjern dét.
            mylist.remove(mylist[0])

            # Lav URL med tilfældigt valgt link til streamingside
            streamLink = "http://watchseries.lt" + random.choice(mylist)
            episodeinfo2.append(streamLink)

            return episodeinfo2


def link2():  # Funktion der åbner den faktiske streamingside
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    # Suk
    episodeinfo3 = link1()
    response = opener.open(episodeinfo3[5])
    html = response.read()
    myList2 = []
    soup = BeautifulSoup(html, "lxml")
    # Det her er fucking latterligt.


    for a in soup.find_all('a', href=True, class_="myButton"):
        myList2.extend([a['href']])
    episodeinfo3.append(myList2[0])

    return episodeinfo3

def startbesked():
    #Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    print bcolors.ATBG + bcolors.ATFG + r"""██████╗  █████╗ ███╗   ██╗██████╗  ██████╗ ███╗   ███╗
██╔══██╗██╔══██╗████╗  ██║██╔══██╗██╔═══██╗████╗ ████║
██████╔╝███████║██╔██╗ ██║██║  ██║██║   ██║██╔████╔██║
██╔══██╗██╔══██║██║╚██╗██║██║  ██║██║   ██║██║╚██╔╝██║
██║  ██║██║  ██║██║ ╚████║██████╔╝╚██████╔╝██║ ╚═╝ ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚═╝     ╚═╝

 █████╗ ██████╗ ██╗   ██╗███████╗███╗   ██╗████████╗██╗   ██╗██████╗ ███████╗
██╔══██╗██╔══██╗██║   ██║██╔════╝████╗  ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝
███████║██║  ██║██║   ██║█████╗  ██╔██╗ ██║   ██║   ██║   ██║██████╔╝█████╗
██╔══██║██║  ██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║   ██║   ██║   ██║██╔══██╗██╔══╝0.2
██║  ██║██████╔╝ ╚████╔╝ ███████╗██║ ╚████║   ██║   ╚██████╔╝██║  ██║███████╗
╚═╝  ╚═╝╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝

""" + bcolors.ENDCOLOR


#VELKOMMEN
startbesked()


while True:
    # Suuuuuk
    episodeinfo4 = []
    episodeinfo4 = link2()
    # Hvordan undgår jeg at bruge episodeinfo 1, 2, 3 og 4?!?! Det kan ikke være rigtigt!!

    startbesked()
    #print "__________________________________________________________________________"

    print bcolors.UNDERLINE + bcolors.BOLD + bcolors.OKBLUE + "Season " + episodeinfo4[0] + " episode " + episodeinfo4[1] + " - \'" + episodeinfo4[4] + "\':" + bcolors.ENDCOLOR
    episodetekst = "\'" + episodeinfo4[2] + "\'"

    #Print nydeligt
    dedented_text = textwrap.dedent(episodetekst).strip()
    print textwrap.fill(dedented_text, width=60) + "\n"

    print bcolors.DIM
    cont = raw_input("Do you want to watch this episode? (Y/N): ")
    while cont.lower() not in ("y", "n"):
        cont = raw_input("Do you want to watch this episode? (Y/N): ")
        print bcolors.ENDCOLOR
    if cont == "y":
        print episodeinfo4[6]
        webbrowser.open(episodeinfo4[6], new=0, autoraise=True)
        break
    elif cont == "n":
        startbesked()
        bcolors.DIM
        print "Fair enough! Finding another one..."
        print bcolors.ENDCOLOR


