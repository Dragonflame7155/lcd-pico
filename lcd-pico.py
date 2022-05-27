from machine import Pin
from utime import sleep

#pin setup
rs = Pin(0, Pin.OUT)
rw = Pin(1, Pin.OUT)
enter = Pin(2, Pin.OUT)
b0 = Pin(3, Pin.OUT)
b1 = Pin(4, Pin.OUT)
b2 = Pin(5, Pin.OUT)
b3 = Pin(6, Pin.OUT)
b4 = Pin(7, Pin.OUT)
b5 = Pin(8, Pin.OUT)
b6 = Pin(9, Pin.OUT)
b7 = Pin(10, Pin.OUT)

#letters
A = [1, 0, 0, 0, 0, 0, 1, 0]
B = [0, 1, 0, 0, 0, 0, 1, 0]
C = [1, 1, 0, 0, 0, 0, 1, 0]
D = [0, 0, 1, 0, 0, 0, 1, 0]
E = [1, 0, 1, 0, 0, 0, 1, 0]
F = [0, 1, 1, 0, 0, 0, 1, 0]
G = [1, 1, 1, 0, 0, 0, 1, 0]
H = [0, 0, 0, 1, 0, 0, 1, 0]
I = [1, 0, 0, 1, 0, 0, 1, 0]
J = [0, 1, 0, 1, 0, 0, 1, 0]
K = [1, 1, 0, 1, 0, 0, 1, 0]
L = [0, 0, 1, 1, 0, 0, 1, 0]
M = [1, 0, 1, 1, 0, 0, 1, 0]
N = [0, 1, 1, 1, 0, 0, 1, 0]
O = [1, 1, 1, 1, 0, 0, 1, 0]
P = [0, 0, 0, 0, 1, 0, 1, 0]
Q = [1, 0, 0, 0, 1, 0, 1, 0]
R = [0, 1, 0, 0, 1, 0, 1, 0]
S = [1, 1, 0, 0, 1, 0, 1, 0]
T = [0, 0, 1, 0, 1, 0, 1, 0]
U = [1, 0, 1, 0, 1, 0, 1, 0]
V = [0, 1, 1, 0, 1, 0, 1, 0]
W = [1, 1, 1, 0, 1, 0, 1, 0]
X = [0, 0, 0, 1, 1, 0, 1, 0]
Y = [1, 0, 0, 1, 1, 0, 1, 0]
Z = [1, 1, 0, 1, 1, 0, 1, 0]
a = [1, 0, 0, 0, 0, 1, 1, 0]
b = [0, 1, 0, 0, 0, 1, 1, 0]
c = [1, 1, 0, 0, 0, 1, 1, 0]
d = [0, 0, 1, 0, 0, 1, 1, 0]
e = [1, 0, 1, 0, 0, 1, 1, 0]
f = [0, 1, 1, 0, 0, 1, 1, 0]
g = [1, 1, 1, 0, 0, 1, 1, 0]
h = [0, 0, 0, 1, 0, 1, 1, 0]
i = [1, 0, 0, 1, 0, 1, 1, 0]
j = [0, 1, 0, 1, 0, 1, 1, 0]
k = [1, 1, 0, 1, 0, 1, 1, 0]
l = [0, 0, 1, 1, 0, 1, 1, 0]
m = [1, 0, 1, 1, 0, 1, 1, 0]
n = [0, 1, 1, 1, 0, 1, 1, 0]
o = [1, 1, 1, 1, 0, 1, 1, 0]
p = [0, 0, 0, 0, 1, 1, 1, 0]
q = [1, 0, 0, 0, 1, 1, 1, 0]
r = [0, 1, 0, 0, 1, 1, 1, 0]
s = [1, 1, 0, 0, 1, 1, 1, 0]
t = [0, 0, 1, 0, 1, 1, 1, 0]
u = [1, 0, 1, 0, 1, 1, 1, 0]
v = [0, 1, 1, 0, 1, 1, 1, 0]
w = [1, 1, 1, 0, 1, 1, 1, 0]
x = [0, 0, 0, 1, 1, 1, 1, 0]
y = [1, 0, 0, 1, 1, 1, 1, 0]
z = [0, 1, 0, 1, 1, 1, 1, 0]

#numbers
n0 = [0, 0, 0, 0, 1, 1, 0, 0]
n1 = [1, 0, 0, 0, 1, 1, 0, 0]
n2 = [0, 1, 0, 0, 1, 1, 0, 0]
n3 = [1, 1, 0, 0, 1, 1, 0, 0]
n4 = [0, 0, 1, 0, 1, 1, 0, 0]
n5 = [1, 0, 1, 0, 1, 1, 0, 0]
n6 = [0, 1, 1, 0, 1, 1, 0, 0]
n7 = [1, 1, 1, 0, 1, 1, 0, 0]
n8 = [0, 0, 0, 1, 1, 1, 0, 0]
n9 = [1, 0, 0, 1, 1, 1, 0, 0]

#symbols
spc = [0, 0, 0, 0, 0, 1, 0, 0]
htg = [1, 1, 0, 0, 0, 1, 0, 0]
dlr = [0, 0, 1, 0, 0, 1, 0, 0]
prc = [1, 0, 1, 0, 0, 1, 0, 0]
aps = [0, 1, 1, 0, 0, 1, 0, 0]
sqt = [1, 1, 1, 0, 0, 1, 0, 0]
mtp = [0, 1, 0, 1, 0, 1, 0, 0]
mns = [0, 0, 1, 1, 0, 1, 0, 0]
fsh = [1, 1, 1, 1, 0, 1, 0, 0]
lst = [0, 0, 1, 1, 1, 1, 0, 0]
eql = [1, 0, 1, 1, 1, 1, 0, 0]
gtt = [0, 1, 1, 1, 1, 1, 0, 0]
att = [0, 0, 0, 0, 0, 0, 1, 0]
bsh = [0, 0, 1, 1, 1, 0, 1, 0]
tth = [0, 1, 1, 1, 1, 0, 1, 0]
usc = [1, 1, 1, 1, 1, 0, 1, 0]
aps = [0, 0, 0, 0, 0, 1, 1, 0]
div = [0, 0, 1, 1, 1, 1, 1, 0]
tld = [0, 1, 1, 1, 1, 1, 1, 0]
cln = [0, 1, 0, 1, 1, 1, 0, 0]
scl = [1, 1, 0, 1, 1, 1, 0, 0]

#brackets
fbr = [0, 0, 0, 1, 0, 1, 0, 0]
bbr = [1, 0, 0, 1, 0, 1, 0, 0]
fsb = [1, 1, 0, 1, 1, 0, 1, 0]
bsb = [1, 0, 1, 1, 1, 0, 1, 0]
fcb = [1, 1, 0, 1, 1, 1, 1, 0]
bcb = [1, 0, 1, 1, 1, 1, 1, 0]

#punctuation
qot = [0, 1, 0, 0, 0, 1, 0, 0]
exc = [1, 0, 0, 0, 0, 1, 0, 0]
prd = [0, 1, 1, 1, 0, 1, 0, 0]
qst = [1, 1, 1, 1, 1, 1, 0, 0]

#commands
clr = [1, 0, 0, 0, 0, 0, 0, 0]
rtn = [0, 1, 0, 0, 0, 0, 0, 0]
clf = [0, 0, 1, 0, 0, 0, 0, 0]
crt = [0, 1, 1, 0, 0, 0, 0, 0]
dlf = [1, 1, 1, 0, 0, 0, 0, 0]
drt = [1, 0, 1, 0, 0, 0, 0, 0]
fln = [0, 1, 0, 0, 0, 0, 0, 0]
sln = [1, 1, 0, 0, 0, 0, 0, 0]
asl = [1, 1, 0, 0, 0, 0, 1, 1]
inittl5x7 = [1, 1, 0, 0, 0, 0, 0, 1]

g0 = [0, 0, 0, 0, 0, 0, 1, 0]
g8 = [0, 0, 0, 1, 0, 0, 1, 0]
g16 = [0, 0, 0, 0, 1, 0, 1, 0]
g24 = [0, 0, 0, 1, 1, 0, 1, 0]
g32 = [0, 0, 0, 0, 0, 1, 1, 0]

smile = [0, 1, 0, 1, 0,
         0, 0, 0, 0, 0,
         1, 0, 0, 0, 1,
         0, 1, 1, 1, 0,
         0, 0 ,0, 0, 0,
         0, 0, 0, 0, 0,
         0, 0, 0, 0, 0,
         0, 0, 0, 0, 0]

cclr = [0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0]
def lcd_init():
    rs.value(0)
    sleep(.0001)
    b0.value(0)
    sleep(.0001)
    b1.value(0)
    sleep(.0001)
    b2.value(1)
    sleep(.0001)
    b3.value(1)
    sleep(.0001)
    b4.value(0)
    sleep(.0001)
    b5.value(0)
    sleep(.0001)
    b6.value(0)
    sleep(.0001)
    b7.value(0)
    sleep(.0001)
    enter.value(1)
    sleep(.002)
    enter.value(0)

def  dispchar(i):
    rs.value(1)
    b0.value(i[0])
    sleep(.0001)
    b1.value(i[1])
    sleep(.0001)
    b2.value(i[2])
    sleep(.0001)
    b3.value(i[3])
    sleep(.0001)
    b4.value(i[4])
    sleep(.0001)
    b5.value(i[5])
    sleep(.0001)
    b6.value(i[6])
    sleep(.0001)
    b7.value(i[7])
    sleep(.0001)
    enter.value(1)
    sleep(.001)
    enter.value(0)

def dispcmd(i):
    rs.value(0)
    b0.value(i[0])
    b1.value(i[1])
    b2.value(i[2])
    b3.value(i[3])
    b4.value(i[4])
    b5.value(i[5])
    b6.value(i[6])
    b7.value(i[7])
    enter.value(1)
    sleep(.001)
    enter.value(0)
    
def clear():
    rs.value(0)
    rw.value(0)
    b0.value(1)
    b1.value(0)
    b2.value(0)
    b3.value(0)
    b4.value(0)
    b5.value(0)
    b6.value(0)
    b7.value(0)
    enter.value(1)
    sleep(.001)
    enter.value(0)
    
def write(message):
    charlist = list(message)
    for i in charlist:
        if i in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            i = "n" + i
        dispchar(globals()[i])
  