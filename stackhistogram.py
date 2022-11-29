import matplotlib.pyplot as plt
import numpy as np

x=np.random.randn(1000,3)
plt.hist(x,30)

plt.xlabel("age")
plt.ylabel("count of people")
plt.title("population count")
plt.show()
