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

    def plot(self, x, y, xf, yf, yNoPeak, yClean):
        fig, axs = plt.subplots(4, 1,figsize=(8,11))
        fig.suptitle('FFT of data from ree API', fontsize=14)
        axs[0].plot(x,y)
        axs[0].set_title('Time domain')
        axs[0].set_xlabel('Time [days]')
        axs[0].set_ylabel('Real demand [MW]')
        axs[0].grid(True)

        axs[1].plot(xf,yf)
        axs[1].set_xlim(0, 6)
        axs[1].set_ylim(0, 20000)
        axs[1].set_title('Frequency domain: FFT of raw signal')
        axs[1].set_xlabel('Frequency [1/day]')
        axs[1].set_ylabel('Amplitude')
        axs[1].grid(True)

        axs[2].plot(xf,yNoPeak)
        axs[2].set_xlim(0, 6)
        axs[2].set_title('Frequency domain: FFT of y = y - mean(y)')
        axs[2].set_xlabel('Frequency [1/day]')
        axs[2].set_ylabel('Amplitude')
        axs[2].grid(True)

        axs[3].plot(xf,yClean)
        axs[3].set_xlim(0, 6)
        axs[3].set_title('Frequency domain: FFT of y = y*window')
        axs[3].set_xlabel('Frequency [1/day]')
        axs[3].set_ylabel('Amplitude')
        axs[3].grid(True)

        fig.tight_layout()
        fig.subplots_adjust(top=0.90)
        plt.savefig('outputImage.png')
        plt.show()
