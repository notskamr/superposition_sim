import math
import matplotlib.pyplot as plt
import numpy as np

SAMPLES = 5000


X_RANGE = float(
    eval(input("Enter x range in radians [eg. 3*pi]: ").replace("pi", str(np.pi))))

phaseDiff1 = float(
    eval(input("Enter phase difference in radians for function 1: ").replace("pi", str(np.pi))))
phaseDiff2 = float(
    eval(input("Enter phase difference in radians for function 2: ").replace("pi", str(np.pi))))

# plot sin and cos superposition
x = np.linspace(-X_RANGE, X_RANGE, SAMPLES)

y1 = np.sin(x + phaseDiff1)
y2 = np.sin(x + phaseDiff2)

plt.figure(num="Superposition")

plt.plot(x, y1, label='Function 1', color='red')
plt.plot(x, y2, label='Function 2', color='blue')
plt.plot(
    x, y1 + y2, label='Superposition', color='green', linestyle='dashed')
plt.legend(loc='upper right', fontsize='small',
           title='Labels', title_fontsize='small')

plt.grid()
plt.show()
