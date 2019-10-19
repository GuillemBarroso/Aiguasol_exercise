from input          import validateInputs
from ree_api        import ReeIndicatorAPI
from FFTcomputation import FFT
import argparse

variableID     = 1293
start_date     = '2018-09-02'
end_date       = '2018-10-06'

parser = argparse.ArgumentParser(description='Read data from ree API and compute FFT')
parser.add_argument('--apiToken', type=str, help='API personal_token',default = '')
parser.add_argument('--force', help='Force download', action = 'store_true')
args           = parser.parse_args()
personal_token = args.apiToken
forceDownload  = args.force

# Validate input data
inputs = validateInputs(start_date,end_date,variableID,personal_token)

# Request ree API
indicator       = ReeIndicatorAPI()
TDvalues, dates = indicator.read(inputs,forceDownload)

# Compute FFT
totalDays = inputs.totalDays
FFT().compute(TDvalues, dates, totalDays)
