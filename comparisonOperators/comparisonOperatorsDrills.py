'''
Created on Jan 29, 2022

@author: ITAUser
'''

b = ("dog" == "cat") 
print (b) 

c = (1.24 == 1.25)
print (c) 

d = ("True" == "False")
print (d) 

e = ([1,2,3] == [1,2,3])
print (e) 

f = (1 <= 2)
print (f) 

g = (1 >= 2)
print (g) 

h = (1.66 >= 1.67)
print (h) 

i = (1.66 <= 1.67)
print (i) 

j = (1 < 2)
print (j) 

k = (1 > 2)
print (k)

l = (11 / 3 < 100 / 33)
print (l)

m = (9 * 7 > 8 * 8)
print (m) 

n = (3 < 1.5 ** 2)
print (n) 

o = 8 * 3
p = 56 / 2
q = (o > p)
print (q) 

import math

r = math.sqrt(96)
s = 8.6 ** 2
t = (r >= s)

'''
#1) 4 == 5 
False

#2) 5 == 5
True

#3) 3 == 3
True

#4) a = 2
# ) a == 2
True

#5) a = 3
# ) b = 2
# ) a == b
False

#6) a = 4
# ) b = 4
# ) a == b
True

#7) a = 6
# ) b = (12/2)
# ) a == b
True

#8) a = (3/3)
# ) b = (13/13)
# ) a == b
True

#9) a = 3
# ) b = 9 / 3
# ) a == b
True

#10) a = "word"
#  ) b = "Word"
#  ) a == b
False

#11) (10/5) == (12/6)
True

#12) (14/7) == (15/5)
False

#13) a = 10
#  ) b = 5
#  ) (a/b) == 2
True

#14) a = 10
#  ) b = 5
#  ) (a/b) == (12/6)
True

#15) a = 10
#  ) b = 5
#  ) c = 12
#  ) d = 6
#  ) (a/b) == (12/6)
True

#16) a = "something"
#  ) b = "some thing"
#  ) a == b
False

#17) a = "word"
#  ) b = "word"
#  ) a == b
True

#18) a = True
#  ) a == True
True

#19) a = True
#  ) b = False
#  ) a == b
False

#20) a = True
#  ) A = False
#  ) b = False
#  ) A == b
True

'''