from datetime import *


class Event:
    def __init__(self, name, startTime, endTime):
        self.name = name
        self.startTime = startTime
        self.endTime = endTime
        self.venue = []

    def addVenue(self, venue):
        self.venue.append(venue)


class Venue:
    def __init__(self, name):
        self.name = name
        self.address = []

    def addAddress(self, address):
        self.address.append(address)


class Address:
    def __init__(self, street, city, state, country, zipcode):
        self.street = street
        self.city = city
        self.state = state
        self.country = country
        self.zipcode = zipcode


event = Event("18th birthday party", time(18, 30), time(00, 00))
venue = Venue("Restaurant")
address = Address("1 Cool Street", "London", "Greater London", "UK", "NW1")

event.addVenue(venue)
venue.addAddress(address)

for eachVenue in event.venue:
    print(eachVenue.name)
    for eachAddress in venue.address:
        print(eachAddress.street)
        print(eachAddress.city)
        print(eachAddress.zipcode)


