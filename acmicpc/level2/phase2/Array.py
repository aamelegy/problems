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
    

n=read_integer()
l=read_integers()
n,p,z=[],[],[]
n=[x for x in l if x<0]
p=[x for x in l if x>0]
z=[x for x in l if x==0]
if len(p)==0:
    p.append(n.pop())
    p.append(n.pop())
if len(n)%2==0:
    z.append(n.pop())
for l in n,p,z:
    print len(l),' '.join(map(str,l))
            
    