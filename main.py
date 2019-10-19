from input   import InputValidation
from ree_api import ReeIndicatorAPI

variableID     = 1293
start_date     = '2015-08-15'
end_date       = '2015-08-16'
personal_token = '650647858608a4659e7016e3164644efb1b70880313267d4a3ac6cd93e2ad691'

start_date_obj,end_date_obj = InputValidation().validate(start_date,end_date,variableID,personal_token)

indicator = ReeIndicatorAPI()
data      = indicator.read(variableID, start_date_obj, end_date_obj, personal_token)

demandValues = data['indicator']['values']

for item in data['indicator']['values']:
    print(item['value'],'; ',item['datetime'])
