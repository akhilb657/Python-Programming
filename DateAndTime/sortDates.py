from datetime import *
import time

startTime = time.perf_counter()
dates = []

d1 = date(2024,9,30)
d2 = date(2020,9,12)
d3 = date(2019,1,12)

dates.append(d1)
dates.append(d2)
dates.append(d3)

dates.sort()

time.sleep(4)

for d in dates:
    print(d)

endTime = time.perf_counter()

print("Execution Time:",endTime-startTime)