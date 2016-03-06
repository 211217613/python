import matplotlib.pyplot as plt
import numpy as np
t = np.arange(-1000,1000)

f1 = t**2
f2 = 1000*t
plt.plot(t, f1, t, f2)

plt.show()
