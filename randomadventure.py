#!/usr/bin/python
# -*- coding: utf-8 -*-

# SOMEONE PLEASE FORK THIS! I CANT STAND LOOKING AT IT! SO. BADLY. CODED. *crying*


import os
import webbrowser
import json
import urllib2
from urllib2 import Request, urlopen, URLError
# from bs4 import BeautifulSoup
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


def randomAdventure():  # Funktion der finder et tilfældigt afsnit og dets info vha. Adventure Time API
    print "Getting super random numbers from the internetz. Please wait..."
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'randomAdventure 0.3')]

    # Åbn forbindelse
    response = opener.open("http://adventuretimeapi.com/api/v1/episodes/")

    # Parse JSON fra webserveren
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

        # Hvis ikke episodevariablen indeholder noget, har vi fået en comic eller lign. fra serveren
        if episode is not None:
            break
        elif episode is None:
            print "The Adventure Time API gave us something that wasn\'t an episode. Maybe a comic. Trying again...\n"

    # Sammensæt url med tilfældige tal
    url = "http://kisscartoon.me/Cartoon/Adventure-Time-with-Finn-Jake-Season-0" + str(season) + "/Episode-0" + str(
            episode)

    # Saml data om episoden i et dictionary
    episodeInfo = {'season': str(season), 'episode': str(episode), 'description': description, 'url': url,
                   'title': title};

    # Return dictionary med episodedata
    return episodeInfo


def startbesked():
    # Clear screen
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
██╔══██║██║  ██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║   ██║   ██║   ██║██╔══██╗██╔══╝0.3
██║  ██║██████╔╝ ╚████╔╝ ███████╗██║ ╚████║   ██║   ╚██████╔╝██║  ██║███████╗
╚═╝  ╚═╝╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝
(Kisscartoon.me Version)
""" + bcolors.ENDCOLOR


# VELKOMMEN
startbesked()

# Primært funktionalitetsloop
while True:
    # Hent data fra randomAdventure() og gem det i episodeInfo variablen
    episodeInfo = randomAdventure()

    # Print startbesked
    startbesked()
    # print "__________________________________________________________________________"

    # Print info om episoden
    print bcolors.UNDERLINE + bcolors.BOLD + bcolors.OKBLUE + "Season " + episodeInfo['season'] + " episode " + \
          episodeInfo['episode'] + " - \'" + episodeInfo['title'] + "\':" + bcolors.ENDCOLOR
    episodetekst = "\'" + episodeInfo['description'] + "\'"

    # Print nydeligt
    dedented_text = textwrap.dedent(episodetekst).strip()
    print textwrap.fill(dedented_text, width=60) + "\n"

    print bcolors.DIM
    cont = raw_input("Do you want to watch this episode? (Y/N): ")
    while cont.lower() not in ("y", "n"):
        cont = raw_input("Do you want to watch this episode? (Y/N): ")
        print bcolors.ENDCOLOR
    if cont == "y":
        print ""
        print "Opening " + episodeInfo['url']
        webbrowser.open(episodeInfo['url'], new=0, autoraise=True)
        break
    elif cont == "n":
        startbesked()
        bcolors.DIM
        print "Fair enough! Finding another one..."
        print bcolors.ENDCOLOR
