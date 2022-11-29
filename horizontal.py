import matplotlib.pyplot as plt

y=["science","commerce","arts"]
w=[200,300,500]
c=["red","yellow","blue"]
plt.barh(y,w,0.4,color=c)
plt.xlabel("courses")
plt.ylabel("student enrolled")
plt.title("student record")
plt.show()