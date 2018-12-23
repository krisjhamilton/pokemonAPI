#!/usr/bin/env python3

from pokemontcgsdk import Card
# from pokemontcgsdk import Set
# from pokemontcgsdk import Type
# from pokemontcgsdk import Supertype
# from pokemontcgsdk import Subtype

cards = Card.where(page=5, pageSize=100)
print(card)
