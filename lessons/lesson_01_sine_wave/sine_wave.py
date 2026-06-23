import numpy as np
import matplotlib.pyplot as plt

A = 5
f = 1

t = np.linspace(0, 2, 1000)

y = A * np.sin(2 * np.pi * f * t)

plt.plot(t, y)
plt.xlabel("Time, s")
plt.ylabel("Float height, cm")
plt.title("Sine wave: float oscillation")
plt.grid(True)
plt.show()