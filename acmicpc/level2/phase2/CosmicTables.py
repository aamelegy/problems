#timelimit
from __future__ import division
import sys
from collections import namedtuple #x=namedtuple('point','x y')
from math import *
from collections import deque, OrderedDict #append #popleft
from fractions import gcd
from copy import copy ,deepcopy
from collections import Counter #Counter(list)
import re #re.split("[^a-zA-Z]",text)
from decimal import Decimal
# from functools import lru_cache #@lru_cache(maxsize = None)
"""
#reduce(func,list)
#map(func,list)
#filter(func,list)
#xor=lambda x,y :x^y
#sign = lambda x: math.copysign(1, x)
#list.reverse() 
#list.sort() list=sorted(list)
list.sort(key=operator.itemgetter(1,2))
#reverse word word[::-1]
#word.islower()
#word.lower() word.upper()
x = x1 if exp1 else x2
any([false,true])
all([true,false])
"a".isalpha()
"1".isdigit()
int(str,base)
"""
 
 
fin=sys.stdin ;fout=sys.stdout 
# fin=open('../in','r') ; fout=open('../out','w')
def readline():
    return fin.readline().strip()
def readstrings():
    return fin.readline().strip().split(' ')
def writeline(value):
    fout.write(str(value))
    fout.write("\n")
def read_integers():
    return [int(x) for x in fin.readline().strip().split(' ')]
def read_integer():
    return int(fin.readline().strip())
def end():
    sys.exit()
def readbig():
    return [Decimal(x) for x in fin.readline().strip().split(' ')]
def write(value):
    fout.write(str(value))
     
 
n,m,k=read_integers()
mat=[]
r_d,c_d=[i for i in xrange(n)],[i for i in xrange(m)]
[mat.append(raw_input().split()) for i in xrange(n)]
for i in xrange(k):
    com=readstrings()
    s,x,y=com[0],int(com[1])-1,int(com[2])-1
    if s=='c':
        c_d[x],c_d[y] =c_d[y],c_d[x]
    elif s=='r':
        r_d[x],r_d[y] = r_d[y],r_d[x]
    else:
        print mat[r_d[x]][c_d[y]]
         
         
 
 
             
     



