addtwo=lambda x,y :x+y
z=addtwo(10,20)
print(z)
print("\n")


list1=[10,20,30,40]
add=list(map(lambda x:x+100,list1))
print(add)
print("\n")

fruits=["apple","banana","apricot","kiwi"]
def start_A(mystr):
    return(mystr[0]=='a')
fruitB=map(start_A,fruits)
print(list(fruitB))
print("\n")


from functools import reduce
l=[10,20,30,40]
x=lambda a,b:a+b
z=reduce(x,l)
print(z)
print("\n")


x=lambda y:y+100
print(x(50))
print("\n")

largest=lambda x,y:x if (x>y)else y
print(largest(10,4))

