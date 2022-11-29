def myfun(n):
    return abs(n-50)
thislist=[100,50,65,85,23]
thislist.sort(key=myfun)
print(thislist)