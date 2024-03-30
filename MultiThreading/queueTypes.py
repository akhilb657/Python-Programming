import queue

q = queue.Queue()
q.put(444)
q.put(111)
q.put(999)
q.put(4455)
while not q.empty():
    print(q.get(),end=' ')

print()

lq = queue.LifoQueue()
lq.put(444)
lq.put(111)
lq.put(999)
lq.put(4455)
while not lq.empty():
    print(lq.get(),end=' ')

print()

pq = queue.PriorityQueue()
pq.put((444,"Ranga"))
pq.put((111,"Reddy"))
pq.put((999,"Kittu"))
pq.put((4455,"Akhil"))
while not pq.empty():
    print(pq.get()[1],end=' ')



