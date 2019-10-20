from datetime import datetime, timedelta

class Input:
    def __init__(self,start_date_obj:datetime, end_date_obj:datetime, indicatorID:int, apiToken:str,totalDays:float):
        self.start_date_obj = start_date_obj
        self.end_date_obj   = end_date_obj
        self.indicatorID    = indicatorID
        self.apiToken       = apiToken
        self.totalDays      = totalDays

def validateInputs(start_date:str, end_date:str, indicatorID:int, apiToken:str):
    # Check that input arguments are valid
    date_format ='%Y-%m-%d'

    try:
        start_date_obj = datetime.strptime(start_date,date_format)
    except ValueError:
        print("Error: Please input date string format YYYY-MM-DD")
        raise

    try:
        end_date_obj   = datetime.strptime(end_date,date_format) + timedelta(days=1) - timedelta(seconds=1)
    except ValueError:
        print("Error: Please input date string format YYYY-MM-DD")
        raise

    if (end_date_obj - start_date_obj) < timedelta(0):
        print("Error: start_date is larger than end_date")
        exit()

    try:
        assert type(indicatorID) == int
    except AssertionError as e:
        e.args += ('Format error:',' Please input an integer as indicatorID')
        raise

    # Compute total time of the sampling
    totalTime = end_date_obj - start_date_obj
    totalDays = totalTime.days

    # If validation is OK return
    return Input(start_date_obj, end_date_obj, indicatorID, apiToken, totalDays)
