import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 180, 1000)
y = np.sin(5*x)
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('sin(5x)')
plt.grid()
plt.show()

#prova di push
