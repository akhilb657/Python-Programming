from datetime import *
class Event:
    def __init__(self,startTime,endTime):
        self.startTime = startTime
        self.endTime = endTime
        self.venue = []
    def addVenue(self,venue):
        self.venue.append(venue)

class Venue:
    def __init__(self,name):
        self.name = name
        self.address = []

    def addAddress(self,address):
        self.address.append(address)

class Address:
    def __init__(self,street,city,state,country,zipcode):
        self.street = street
        self.city = city
        self.state = state
        self.country = country
        self.zipcode = zipcode

event = Event(time(5,30),time(10,30))
venue = Venue("C Conventon")
address = Address("Cross roads","Vijayawda","Andhra Pradesh","india","555555")

event.addVenue(venue)
venue.addAddress(address)

for eachVenue in event.venue:
    print(eachVenue.name)
    for details in eachVenue.address:
        print(details.street)
        print(details.city)
        print(details.state)
        print(details.country)
        print(details.zipcode)

print("Time",event.startTime,"to",event.endTime)