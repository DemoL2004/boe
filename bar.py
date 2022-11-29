import matplotlib.pyplot as plt
from matplotlib.figure import Figure
fruits=["apple","mango","kiwi","orange"]
count=[40,80,35,95]
figure=plt.figure(figsize=(7,5),facecolor='g',edgecolor='b',linewidth=7)
plt.bar(fruits,count)
barlabels=["red","blue","red","orange"]
barcolors=['tab:red','tab:blue','tab:red','tab:orange' ]
plt.bar(fruits,count,label=barlabels,color="red")
plt.show()