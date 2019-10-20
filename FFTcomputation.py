#matplotlib inline
from typing              import List
from scipy.fftpack       import fft
from datetime            import datetime
import matplotlib.pyplot as plt
import numpy             as np

class FFT:
    def compute(self, x, y, totalDays:float):
        # Average timeStep assuming equally-spaced sampling
        numData  = len(y)
        timeStep = totalDays/numData
        xf       = np.linspace(0.0, 1.0/(2.0*timeStep), numData//2)
        yAux     = fft(y)
        yf       = 2.0/numData * np.abs(yAux[0:numData//2])
        return x, y, xf, yf

    def plot(self, x, y, xf, yf):
        fig, axs = plt.subplots(2, 1)
        fig.suptitle('FFT of data from ree API', fontsize=14)
        axs[0].plot(x,y)
        axs[0].set_title('Time domain')
        axs[0].set_xlabel('Time [days]')
        axs[0].set_ylabel('Real demand [MW]')
        axs[0].grid(True)

        axs[1].plot(xf,yf)
        axs[1].set_xlim(0, 6)
        axs[1].set_ylim(0, 20000)
        axs[1].set_title('Frequency domain')
        axs[1].set_xlabel('Frequency [Hz]')
        axs[1].set_ylabel('Amplitude')
        axs[1].grid(True)

        fig.tight_layout()
        fig.subplots_adjust(top=0.88)
        plt.show()
