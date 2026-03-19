from matplotlib import pyplot as plt
import numpy as np

x = np.arange(0, 5, 0.0001)
y = x**2
z = np.sqrt(x)

plt.figure(figsize=(5.5, 2))
plt.subplot(1, 2, 1)
plt.title('x**2')
plt.plot(x, y, 'b')
plt.subplot(1, 2, 2)
plt.title('sqrt(x)')
plt.plot(x, z, 'r')
plt.show()