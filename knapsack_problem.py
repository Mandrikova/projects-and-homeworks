import numpy as np
W, n = map(int, input().split())
w = list(map(int, input().split()))

D = np.zeros((W+1, n+1))
for i in range(1, n+1):
  for j in range(1, W+1):
    D[j, i] = D[j, i-1]
    if (w[i-1] <= j):
      D[j, i] = max(D[j, i], D[j-w[i-1], i-1]+w[i-1])
      
print(int(D[W, n]))