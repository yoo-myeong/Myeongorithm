import heapq

n = int(input())

card_dec = []

for i in range(n):
  heapq.heappush(card_dec, int(input()))

check_cnt = 0

for i in range(len(card_dec)-1):
  x = heapq.heappop(card_dec)
  y = heapq.heappop(card_dec)
  check_cnt += (x+y)
  heapq.heappush(card_dec, x+y)
  
print(check_cnt)
