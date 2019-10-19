from datetime import datetime, timedelta

class InputValidation:
    def validate(self, start_date:str, end_date:str, variableID:int, personal_token:str):
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
            raise

        try:
            assert type(variableID) == int
        except AssertionError as e:
            e.args += ('Format error:',' Please input an integer as variableID')
            raise

        try:
            assert type(personal_token) == str
        except AssertionError as e:
            e.args += ('Format error:',' Please input a string as personal_token')
            raise

        # If validation is OK return
        return start_date_obj, end_date_obj
