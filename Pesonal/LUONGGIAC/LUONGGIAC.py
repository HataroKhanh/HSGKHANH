from math import *
from random import random
a,b=5,4
c={'sin(a+b)':sin(a+b),'sin(a-b)':sin(a-b),'cos(a-b)':cos(a-b),
   'cos(a+b)':cos(a+b),'tan(a-b)':tan(a-b),'tan(a+b)':tan(a+b),}
while 1:
    index = random(0,len())
    print(c[index])



