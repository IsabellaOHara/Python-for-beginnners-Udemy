import queue

# first in first out
q = queue.Queue()
q.put(400)
q.put(100)
q.put(200)
q.put(420)
print(q.size())
while not q.empty():
    print(q.get(), end=' ')
print(q.size())

print()

# last in first out
lq = queue.LifoQueue()
lq.put(400)
lq.put(100)
lq.put(200)
lq.put(420)
while not lq.empty():
    print(lq.get(), end=' ')

print()

# priority
pq = queue.PriorityQueue()
pq.put(400)
pq.put(100)
pq.put(200)
pq.put(420)
while not pq.empty():
    print(pq.get(), end=' ')

print()

# priority - with strings need to put in as tuple then will be sorted by the no.
pq2 = queue.PriorityQueue()
pq2.put((400, "John"))
pq2.put((100, "Bob"))
pq2.put((200, "Jill"))
pq2.put((420, "Pam"))
while not pq2.empty():
    print(pq2.get()[1], end=' ')
