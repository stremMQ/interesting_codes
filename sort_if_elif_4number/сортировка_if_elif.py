a = int(input())
b = a % 10
c = a % 100 // 10
d = a % 1000 // 100
f = a % 10000 // 1000
max,min,mins,maxs = 0,0,0,0
indexmin,indexmax = '', ''
if b >= c and b >= d and b >= f:
    max = b
    indexmax = "b"
elif c >= b and c >= d and c >= f:
    max = c
    indexmax = "c"
elif d >= c and d >= b and d >= f:
    max = d
    indexmax = "d"
elif f >= b and f >= c and f >= d:
    max = f
    indexmax = "f"
if b == 0: b = 1000
if c == 0: c = 1000
if d == 0: d = 1000
if f == 0: f == 1000
if c <= d and c <= f and c <= b:
    min = c
    indexmin = "c"
elif b <= c and b <= f and b <= d:
    min = b
    indexmin = "b"
elif d <= c and d <= b and d <= f:
    min = d
    indexmin = "d"
elif f <= c and f <= b and f <= d:
    min = f
    indexmin = "f"
if b == 1000: b = 0
if c == 1000: c = 0
if d == 1000: d = 0
if f == 1000: f == 0
if indexmin == "b":
    if indexmax == "c":
        if d >= f:
            maxs = d
            mins = f
        else:
            maxs = f
            mins = d
    elif indexmax == "d":
        if c >= f:
            maxs = c
            mins = f
        else:
            maxs = f
            mins = c
    elif indexmax == "f":
        if d >= c:
            maxs = d
            mins = c
        else:
            maxs = c
            mins = d
if indexmin == "c":
    if indexmax == "b":
        if d >= f:
            maxs = d
            mins = f
        else:
            maxs = f
            mins = d
    elif indexmax == "d":
        if b >= f:
            maxs = b
            mins = f
        else:
            maxs = f
            mins = b
    elif indexmax == "f":
        if d >= b:
            maxs = d
            mins = b
        else:
            maxs = b
            mins = d
if indexmin == "d":
    if indexmax == "f":
        if c >= b:
            maxs = c
            mins = b
        else:
            maxs = b
            mins = c
    elif indexmax == "b":
        if c >= f:
            maxs = c
            mins = f
        else:
            maxs = f
            mins = c
    elif indexmax == "c":
        if f >= b:
            maxs = f
            mins = b
        else:
            maxs = b
            mins = f
if indexmin ==  "f":
    if indexmax == "c":
        if d >= b:
            maxs = d
            mins = b
        else:
            maxs = b
            mins = d
    elif indexmax == "d":
        if c >= b:
            maxs = c
            mins = b
        else:
            maxs = b
            mins = c
    elif indexmax == "b":
        if d >= c:
            maxs = d
            mins = c
        else:
            maxs = c
            mins = d
print(min,mins,maxs,max)