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


points = random.sample(range(1000), 1000)
function = noisy_signal(x)

gf_min = function[0]
gx_min = 0
for x in points[2:]:
    if function[x] < gf_min:
        gf_min = function[x]
        gx_min = x
print(f'Global minimum, x: {gx_min}, y: {gf_min}')
fig, axis = plt.subplots()

axis.plot(t, function, linewidth=2.0)

plt.show()
