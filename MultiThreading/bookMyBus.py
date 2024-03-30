from threading import *

class BookMyBus:

    def __init__(self, availableSeats):
        self.availableSeats = availableSeats
        self.l = Semaphore()
    def buy(self, seatsRequiried):
        self.l.acquire()
        print("Total seats available: ",self.availableSeats)
        if (self.availableSeats >= seatsRequiried):
            print("select a seat")
            print("processing payment")
            print("printing the ticket")
            self.availableSeats -= seatsRequiried
        else:
            print("OOPS! No Seats Available")
        self.l.release()

obj = BookMyBus(10)
t1 = Thread(target=obj.buy,args=(3,))
t2 = Thread(target=obj.buy,args=(4,))
t3 = Thread(target=obj.buy,args=(4,))

t1.start()
t2.start()
t3.start()