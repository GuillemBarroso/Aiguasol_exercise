from input          import validateInputs
from ree_api        import ReeIndicatorAPI
from FFTcomputation import FFT

variableID     = 1293
start_date     = '2018-09-02'
end_date       = '2018-10-06'
personal_token = '650647858608a4659e7016e3164644efb1b70880313267d4a3ac6cd93e2ad691'

# Validate input data
inputs = validateInputs(start_date,end_date,variableID,personal_token)

# Request ree API
indicator       = ReeIndicatorAPI()
TDvalues, dates = indicator.read(inputs)

# Compute FFT
totalDays = inputs.totalDays
FFT().compute(TDvalues, dates, totalDays)
