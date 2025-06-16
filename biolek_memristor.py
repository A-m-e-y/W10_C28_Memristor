import numpy as np
import matplotlib.pyplot as plt

# Constants
Ron = 100
Roff = 16000
D = 10e-9
mu_v = 1e-14
dt = 1e-5
T = 0.2  # simulate 0.2 sec

frequencies = [10, 20, 30, 100]  # try different input frequencies
colors = ['b', 'g', 'r', 'm']

plt.figure(figsize=(8, 6))

for freq, color in zip(frequencies, colors):
    time = np.arange(0, T, dt)
    v = 1.0 * np.sin(2 * np.pi * freq * time)
    x = 0.5
    i_hist = []
    v_hist = []

    for t in range(len(time)):
        M = Ron * x + Roff * (1 - x)
        i = v[t] / M
        dx = dt * mu_v * Ron / (D**2) * i * (1 - (2 * x - 1)**2)
        x += dx
        x = max(0, min(1, x))
        i_hist.append(i)
        v_hist.append(v[t])

    plt.plot(v_hist, i_hist, color=color, label=f"{freq} Hz")

plt.title("Memristor I-V Hysteresis at Varying Frequencies")
plt.xlabel("Voltage (V)")
plt.ylabel("Current (A)")
plt.legend()
plt.grid(True)
plt.tight_layout()
# plt.show()

plt.savefig("biolek_memristor_iv.png")  # Save the plot as a PNG file
plt.show()
