def ExtractMax():
  heap[0], heap[len(heap)-1] = heap[len(heap)-1], heap[0]
  res = heap.pop(len(heap)-1)
  i = 0
  while (i < len(heap)-1):
    if (i*2+1 == len(heap)-1) and (heap[i] < heap[len(heap)-1]):
      heap[i], heap[len(heap)-1] = heap[len(heap)-1], heap[i]
    if (i*2+1 >= len(heap)-1):
      break
    if (heap[i]>heap[i*2+1]) and (heap[i]>heap[(i+1)*2]):
      break
    if (heap[(i+1)*2]>heap[i*2+1]):
      k = (i+1)*2
    else:
      k = i*2+1
    heap[k], heap[i] = heap[i], heap[k]
    i = k
  return res
  
def Insert(x):
  heap.append(x)
  i = len(heap)-1
  while (i > 0) and (heap[i] > heap[(i+1)//2-1]):
    heap[(i+1)//2-1], heap[i] = heap[i], heap[(i+1)//2-1]
    i = (i+1)//2-1

heap = []  
n = int(input())
for i in range(n):
  q = input()
  if q[:6] == "Insert":
    Insert(int(q.split()[1]))
  else: 
    print(ExtractMax())