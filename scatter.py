import matplotlib.pyplot as plt
from matplotlib.figure import Figure

x=[1,2,3,4,5,6]
y=[100,70,10,50,30,20]
size=[10,100,20,90,50,70]

plt.scatter(x,y,s=size,alpha=1,color='orange',label="2020")
plt.xlabel("x-value")
plt.ylabel("y-value")
plt.title("scatter graph")
plt.legend()
plt.show()