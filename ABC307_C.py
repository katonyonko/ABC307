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
3 5
#.#..
.....
.#...
2 2
#.
.#
5 3
...
#.#
.#.
.#.
...
2 2
#.
.#
2 2
#.
.#
2 2
##
##
1 1
#
1 2
##
1 1
#
3 3
###
...
...
3 3
#..
#..
#..
3 3
..#
..#
###
"""

def solve(test):
  HA,WA=map(int,input().split())
  A=[input() for _ in range(HA)]
  A=[[1 if A[i][j]=='#' else 0 for j in range(WA)] for i in range(HA)]
  HB,WB=map(int,input().split())
  B=[input() for _ in range(HB)]
  B=[[1 if B[i][j]=='#' else 0 for j in range(WB)] for i in range(HB)]
  HX,WX=map(int,input().split())
  X=[input() for _ in range(HX)]
  X=[[1 if X[i][j]=='#' else 0 for j in range(WX)] for i in range(HX)]
  ans='No'
  for ia in range(HX+2*HA-2):
    for ja in range(WX+2*WA-2):
      flga=0
      for iaa in range(HA):
        p=iaa-(HA-1-ia)
        for jaa in range(WA):
          q=jaa-(WA-1-ja)
          if A[iaa][jaa]==1 and (p<0 or p>=HX or q<0 or q>=WX): flga=1
      if flga==1: continue
      for ib in range(HX+2*HB-2):
        for jb in range(WX+2*WB-2):
          flgb=0
          for ibb in range(HB):
            p=ibb-(HB-1-ib)
            for jbb in range(WB):
              q=jbb-(WB-1-jb)
              if B[ibb][jbb]==1 and (p<0 or p>=HX or q<0 or q>=WX): flgb=1
          if flgb==1: continue
          flg=0
          for ix in range(HX):
            for jx in range(WX):
              m=0
              iia,jja=HA-1-ia+ix,WA-1-ja+jx
              iib,jjb=HB-1-ib+ix,WB-1-jb+jx
              if 0<=iia<HA and 0<=jja<WA: m|=A[iia][jja]
              if 0<=iib<HB and 0<=jjb<WB: m|=B[iib][jjb]
              if m!=X[ix][jx]: flg=1
          if flg==0:
            ans='Yes'
  if test==0:
    print(ans)
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