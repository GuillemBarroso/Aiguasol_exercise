#matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack

# Number of samplepoints
N = 600
# sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x) +  0.5*np.cos(200.0 * 2.0*np.pi*x)
yf = scipy.fftpack.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)




#plt.subplot(2, 1, 1)
fig, ax = plt.subplots()
ax.plot(xf, 2.0/N * np.abs(yf[:N//2]))
#plt.title('Test plot 1')
#plt.ylabel('Time [units?]')

#plt.subplot(2, 1, 2)
#ax.plot(xf, 2.0/N * np.abs(yf[:N//2]))
#plt.xlabel('Frequency [Hz]')
#plt.ylabel('Test plot 2')
plt.show()
