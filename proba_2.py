import numpy as np
from scipy.signal import chirp, spectrogram
import matplotlib.pyplot as plt
t = np.linspace(60, 100, 30)
w = chirp(t, f0=2, f1=8.2, t1=2, method='linear')
plt.plot(t, w)
plt.title("Linear Chirp")
plt.xlabel('time in sec)')

plt.show()