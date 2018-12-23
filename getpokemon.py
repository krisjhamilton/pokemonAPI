#!/usr/bin/env python3

import requests
from pokemontcgsdk import Card
# from pokemontcgsdk import Set
# from pokemontcgsdk import Type
# from pokemontcgsdk import Supertype
# from pokemontcgsdk import Subtype

# requests.packages.urllib3.disable_warnings()

import traceback

#This line opens a log file
log = open("log.txt", "w")

try:
    # some code
    # Below line will print any print to log file as well.
    session = requests.Session()
    session.verify = False

    cards = Card.where(page=5, pageSize=100)
    print(card)
    print("Creating DB Connection", file = log)
except Exception:
    traceback.print_exc(file=log)


