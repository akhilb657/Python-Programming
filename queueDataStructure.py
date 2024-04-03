import queue

q = queue.Queue()

q.put("Python")
q.put("Django")
q.put("DRF")
q.put("Azure")

print(q.queue)
q.queue.clear()

print(q.qsize())
while not q.empty():
    print(q.get())

print(q.qsize())