import matplotlib.pyplot as plt
from matplotlib.figure import Figure
x=["india","australia","german","usa"]
y=[45,15,25,20]
fig=plt.figure(figsize=(10,7))
plt.plot()
plt.pie(y,labels=x)
plt.show()
