from urllib.request import Request, urlopen
from datetime       import datetime
from input          import Input
from os import path, mkdir
import json


date_format ='%Y-%m-%d'
cacheFolder = './cache'

class ReeIndicatorAPI:
    def read(self, inputs:Input):
        variableID     = inputs.variableID
        start_date_obj = inputs.start_date_obj
        end_date_obj   = inputs.end_date_obj
        personal_token = inputs.personal_token

        fileName = self.generateFileName(variableID, start_date_obj, end_date_obj)

        if not self.isCached(fileName):
            start_date = start_date_obj.strftime(date_format)
            end_date   = end_date_obj.strftime(date_format)

            url = 'https://api.esios.ree.es/indicators/{}?start_date={}&end_date={}'.format(variableID,start_date,end_date)
            req = Request(url)
            req.add_header('Accept','application/json; application/vnd.esios-api-v1+json')
            req.add_header('Content-Type','application/json')
            req.add_header('Host','api.esios.ree.es')
            req.add_header('Authorization','Token token="{}"'.format(personal_token))
            req.add_header('Cookie','')

            json_obj = urlopen(req)
            jsonfile = json.load(json_obj)

            TDvalues, dates = self.unpackJson(jsonfile)

            self.writeCache(fileName, jsonfile)

            print('Returning from API')
            return TDvalues, dates
        else:
            print('Returning from cache')
            return self.readCache(fileName)

    def isCached(self, fileName:str):
        return path.exists(fileName)

    def writeCache(self,fileName:str, data):
        if not path.exists(cacheFolder):
            mkdir(cacheFolder,755)
        with open(fileName, 'w+') as outputfile:
            json.dump(data,outputfile)

    def generateFileName(self,variableID:int, start_date_obj:datetime, end_date_obj:datetime):
        start_date = start_date_obj.strftime(date_format)
        end_date   = end_date_obj.strftime(date_format)
        return '{}/data_{}_{}_{}.txt'.format(cacheFolder,variableID,start_date,end_date)

    def readCache(self, fileName:str):
        with open(fileName) as jsonfile:
            return self.unpackJson(json.load(jsonfile))

    def unpackJson(self,jsonfile):
        TDvalues = []
        dates    = []

        for item in jsonfile['indicator']['values']:
            TDvalues.append(item['value'])
            dates.append(item['datetime'])

        return TDvalues, dates
