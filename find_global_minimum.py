import random

import matplotlib.pyplot as plt
import numpy as np

n = 1000
t = np.linspace(-3, 3, n)
np.random.seed(2)

x = np.cos(30 * t) + np.sin(10 * t) + 0.3 * (t ** 2)


def noisy_signal(signal):
    return np.random.normal(0, 0.2, len(signal)) + signal

# Monte-Carlo Method

def f(x):
    return

points = random.sample(range(1000), 1000)
print(points[0])
x_ref = noisy_signal(points[0])

for x in points[2:]:
    if noisy_signal(x) < x_ref:
        x_ref = noisy_signal(x)

fig, axis = plt.subplots()

axis.plot(t, noisy_signal(x), linewidth=2.0)

plt.show()
