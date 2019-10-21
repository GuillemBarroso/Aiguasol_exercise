from FFTcomputation      import FFT
import numpy             as np
import matplotlib.pyplot as plt
from scipy.fftpack       import fft as fastFT

# Number of sample points
N = 600
# sample spacing (equally-spaced)
T = 1.0 / 800.0

x = np.linspace(0.0, N*T, N)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)

fft          = FFT()
x, y, xf, yf = fft.compute(x, y, T*N)

# Plot
fig, axs = plt.subplots(2, 1)
fig.suptitle('Test problem: $y(x) = sin(50*2*pi*x) + 0.5*sin(80*2*pi*x)$', fontsize=14)
axs[0].plot(x,y)
axs[0].set_title('Time domain')
axs[0].set_xlabel('$x$')
axs[0].set_ylabel('$y(x)$')
axs[0].grid(True)

axs[1].plot(xf,yf)
axs[1].set_title('Frequency domain')
axs[1].set_xlabel('Frequency [Hz]')
axs[1].set_ylabel('Amplitude')
axs[1].grid(True)

fig.tight_layout()
fig.subplots_adjust(top=0.88)
plt.savefig('outputImage_testFFT.png')
plt.show()
