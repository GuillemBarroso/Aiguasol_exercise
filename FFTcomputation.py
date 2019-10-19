#matplotlib inline
from typing              import List
from scipy.fftpack       import fft, fftfreq
from datetime            import datetime
import numpy             as np
import matplotlib.pyplot as plt

class FFT:
    def compute(self, TDvalues:List[int], dates:List[str], totalDays):
        # Average timeStep assuming equally-spaced sampling
        numData  = len(dates)
        timeStep = totalDays/numData
        x        = np.linspace(0.0, totalDays, numData)
        y        = np.array(TDvalues)

        xf     = np.linspace(0.0, 1.0/(2.0*timeStep), numData/2)
        yf     = fft(y)
        yfPlot = 2.0/numData * np.abs(yf[:numData//2])

        # PLOT
        fig, axs = plt.subplots(2, 1)
        axs[0].plot(x,y)
        axs[0].set_xlabel('Time [days]')
        axs[0].set_ylabel('Real demand [MW]')
        axs[0].grid(True)

        axs[1].plot(xf,yfPlot)
        axs[1].set_xlim(0, 6)
        axs[1].set_ylim(0, 20000)
        axs[1].set_xlabel('Frequency [Hz]')
        axs[1].set_ylabel('Amplitude')
        axs[1].grid(True)

        fig.tight_layout()
        plt.show()
