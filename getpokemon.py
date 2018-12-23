#!/usr/bin/env python3

import requests
import traceback

from pokemontcgsdk import Card
# from pokemontcgsdk import Set
# from pokemontcgsdk import Type
# from pokemontcgsdk import Supertype
# from pokemontcgsdk import Subtype

# requests.packages.urllib3.disable_warnings()

log = open("log.txt", "w")
session = requests.Session()
session.verify = False

try:
    cards = Card.where(page=5, pageSize=100)
    print(card)

except Exception:
    traceback.print_exc(file=log)


