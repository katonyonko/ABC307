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
8
a(b(d))c
5
a(b)(
2
()
6
)))(((
"""

def solve(test):
  N=int(input())
  S=input()
  ans=[]
  tmp=[]
  for i in range(N):
    if S[i]=='(':
      tmp.append(i)
    elif S[i]==')':
      if len(tmp)>0:
        j=tmp.pop()
        while len(ans)>0 and j<ans[-1][0] and ans[-1][1]<i+1: ans.pop()
        ans.append((j,i+1))
  ans2=[]
  if len(ans)>0:
    if ans[0][0]>0: ans2.append((0,ans[0][0]))
    for i in range(len(ans)-1): ans2.append((ans[i][1],ans[i+1][0]))
    if ans[-1][1]<N: ans2.append((ans[-1][1],N))
  else: ans2.append((0,N))
  if test==0:
    print(''.join([S[ans2[i][0]:ans2[i][1]] for i in range(len(ans2))]))
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