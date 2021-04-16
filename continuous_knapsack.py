n, w = map(int, input().split())

cw = [[int(x) for x in input().split()] for i in range(n)]
cw.sort(key=lambda x: x[0]/x[1], reverse = True)
S = 0
W = 0
for i in range(n):
  w_dop = w-W
  if (cw[i][1 ]<= w_dop):
    S += cw[i][0]
    W += cw[i][1]
  else:
    S += cw[i][0]/cw[i][1]*w_dop
    break
print('{:.3f}'.format(S))