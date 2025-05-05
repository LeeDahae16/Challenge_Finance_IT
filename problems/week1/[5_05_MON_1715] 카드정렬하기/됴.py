import heapq

N = int(input())
cards = [int(input()) for i in range(N)]

heapq.heapify(cards)

total = 0
while len(cards)>1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    s = a+b
    total += s
    heapq.heappush(cards, s)

print(total)