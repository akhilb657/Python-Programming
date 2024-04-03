import queue

lq = queue.LifoQueue()

lq.put("Azure")
lq.put("DRF")
lq.put("Django")
lq.put("Python")

print(lq.queue)

while not lq.empty():
    print(lq.get())

print(lq.qsize())