from functools import reduce
fiblist=[1,1,2,3,5,8,13,21,34,55]
odd_num=lambda x:x%2
fibodd=list(map(odd_num,fiblist))
print(fibodd)
sum=lambda x,y:x+y
sumoddfib=reduce(sum,fibodd)
print(sumoddfib)