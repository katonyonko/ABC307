import io
import sys
import pdb
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations, accumulate
from heapq import heappush, heappop
sys.setrecursionlimit(10**6)
from bisect import bisect_right, bisect_left
from math import gcd
import math

_INPUT = """\
6
4 4
1 2 2
2 3 1
2 4 3
3 4 2
1
1
2
3 3
7 7
1 2 2
2 3 3
3 4 1
4 5 1
5 6 3
3 7 1
4 7 1
2
1 6
2
2 3
5 1
1 2 5
2
1 3
3
3 7 5
"""

def solve(test):
  N,M=map(int,input().split())
  G=[[] for _ in range(N)]
  for _ in range(M):
    U,V,W=map(int,input().split())
    U-=1; V-=1
    G[U].append((W,V))
    G[V].append((W,U))
  for i in range(N):
    G[i].sort(reverse=True)
  K=int(input())
  A=list(map(lambda x:int(x)-1,input().split()))
  h=[]
  edge=[]
  inf=10**20
  done=[-1]*N
  C=[inf]*N
  for i in range(K):
    for w,v in G[A[i]]:
      heappush(edge,(w,v))
    C[A[i]]=0
    done[A[i]]=0
  D=int(input())
  X=list(map(int,input().split()))
  for i in range(D):
    while len(edge)>0 and edge[0][0]<=X[i]:
      w,v=heappop(edge)
      heappush(h,(w,v))
      C[v]=min(C[v],w)
    tmp=[]
    while h:
      x,y=heappop(h)
      if done[y]>-1: continue
      done[y]=i+1
      tmp.append(y)
      for w,v in G[y]:
        heappush(edge,(w,v))
      while len(G[y])>0 and C[y]+G[y][-1][0]<=X[i]:
        w,v=G[y].pop()
        if C[v]>C[y]+w:
          C[v]=C[y]+w
          heappush(h,(C[v],v))
    for j in range(len(tmp)):
      C[tmp[j]]=0
  ans=done
  if test==0:
    print(*ans,sep='\n')
  else:
    return None

def random_input():
  from random import randint,shuffle
  N=randint(1,10)
  M=randint(1,N)
  A=list(range(1,M+1))+[randint(1,M) for _ in range(N-M)]
  shuffle(A)
  return (" ".join(map(str, [N,M]))+"\n"+" ".join(map(str, A))+"\n")*3

def simple_solve():
  return []

def main(test):
  if test==0:
    solve(0)
  elif test==1:
    sys.stdin = io.StringIO(_INPUT)
    case_no=int(input())
    for _ in range(case_no):
      solve(0)
  else:
    for i in range(1000):
      sys.stdin = io.StringIO(random_input())
      x=solve(1)
      y=simple_solve()
      if x!=y:
        print(i,x,y)
        print(*[line for line in sys.stdin],sep='')
        break

#0:提出用、1:与えられたテスト用、2:ストレステスト用
main(0)