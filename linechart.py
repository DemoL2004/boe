import matplotlib.pyplot as plt
from matplotlib.figure import Figure
x=[20,40,60,80,100]
y=[1000,2000,3000,4000,5000]

plt.xlabel("x-value")
plt.ylabel("y-value")
plt.title("our-analysis")
plt.xticks(x,labels=["one","two","three","four","five"])
plt.yticks(y,labels=["one","two","three","four","five"])
figure=plt.figure(figsize=(7,5),facecolor='g',edgecolor='b',linewidth=7)
ax=figure.add_axes([1,1,1,1])
ax1=figure.add_axes([2,1,1,1])
ax.plot(x,y)
ax1.plot(x,y)

plt.plot(x,y,'ro')
plt.show()