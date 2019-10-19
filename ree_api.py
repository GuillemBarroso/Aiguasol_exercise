from urllib.request import Request, urlopen
from datetime       import datetime
import json

date_format ='%Y-%m-%d'

class ReeIndicatorAPI:
    def read(self, variableID:int, start_date_obj:datetime, end_date_obj:datetime, personal_token:str):
        start_date = start_date_obj.strftime(date_format)
        end_date   = end_date_obj.strftime(date_format)

        url = 'https://api.esios.ree.es/indicators/{}?start_date={}&end_date={}'.format(variableID,start_date,end_date)
        req = Request(url)
        req.add_header('Accept','application/json; application/vnd.esios-api-v1+json')
        req.add_header('Content-Type','application/json')
        req.add_header('Host','api.esios.ree.es')
        req.add_header('Authorization','Token token="{}"'.format(personal_token))
        req.add_header('Cookie','')

        #return urlopen(req).read()

        json_obj = urlopen(req)
        return json.load(json_obj)
