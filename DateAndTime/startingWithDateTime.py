import time, datetime

epochSec = time.time()
print(epochSec)

t = time.ctime(epochSec)
print(t)

dt = datetime.datetime.today()
print("Curent date: {}-{}-{}".format(dt.day, dt.month, dt.year))
print("Current time: {}:{}:{}".format(dt.hour, dt.minute, dt.second))