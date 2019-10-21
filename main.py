from input          import validateInputs
from ree_api        import ReeIndicatorAPI
from FFTcomputation import FFT
import argparse
import numpy        as np
import statistics

indicatorID    = 1293
start_date     = '2018-09-02'
end_date       = '2018-10-06'

parser = argparse.ArgumentParser(description='Read data from ree API and compute FFT')
parser.add_argument('--apiToken', type=str, help='personal API token',default = '')
parser.add_argument('--force', help='Force download', action = 'store_true')
args   = parser.parse_args()

# Validate input data
inputs = validateInputs(start_date, end_date, indicatorID, args.apiToken)

# Request ree API
indicator       = ReeIndicatorAPI()
TDvalues, dates = indicator.read(inputs, args.force)

# Compute FFT
x            = np.linspace(0.0, inputs.totalDays, len(dates))
yRaw         = np.array(TDvalues)
meanValue    = statistics.mean(yRaw)
yNorm        = yRaw - meanValue

window = np.hanning(yNorm.size)
yClean = yNorm*window

fft              = FFT()
x, y, xf, yf     = fft.compute(x, yRaw, inputs.totalDays)
x, y, xf, yNoPeak= fft.compute(x, yNorm, inputs.totalDays)
x, y, xf, yClean = fft.compute(x, yClean, inputs.totalDays)

# Plot solution
fft.plot(x, yRaw, xf, yf, yNoPeak, yClean)
