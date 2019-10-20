from urllib.request import Request, urlopen
from datetime       import datetime
from input          import Input
from os import path, mkdir
import json

date_format ='%Y-%m-%d'
cacheFolder = './cache'

def generateFileName(indicatorID:int, start_date_obj:datetime, end_date_obj:datetime):
    start_date = start_date_obj.strftime(date_format)
    end_date   = end_date_obj.strftime(date_format)
    return '{}/data_{}_{}_{}.txt'.format(cacheFolder,indicatorID,start_date,end_date)

def unpackJson(jsonfile):
    TDvalues = []
    dates    = []

    for item in jsonfile['indicator']['values']:
        TDvalues.append(item['value'])
        dates.append(item['datetime'])

    return TDvalues, dates

class ReeIndicatorAPI:
    def read(self, inputs:Input, forceDownload:bool):
        indicatorID    = inputs.indicatorID
        start_date_obj = inputs.start_date_obj
        end_date_obj   = inputs.end_date_obj
        apiToken       = inputs.apiToken

        fileName = generateFileName(indicatorID, start_date_obj, end_date_obj)
        cache    = Cache(fileName)
        if not cache.isCached(fileName) or forceDownload:
            start_date = start_date_obj.strftime(date_format)
            end_date   = end_date_obj.strftime(date_format)

            url = 'https://api.esios.ree.es/indicators/{}?start_date={}&end_date={}'.format(indicatorID,start_date,end_date)
            req = Request(url)
            req.add_header('Accept','application/json; application/vnd.esios-api-v1+json')
            req.add_header('Content-Type','application/json')
            req.add_header('Host','api.esios.ree.es')
            req.add_header('Authorization','Token token="{}"'.format(apiToken))
            req.add_header('Cookie','')

            json_obj = urlopen(req)
            jsonfile = json.load(json_obj)

            TDvalues, dates = unpackJson(jsonfile)

            cache.writeCache(fileName, jsonfile)

            print('Returning from API')
            return TDvalues, dates
        else:
            print('Returning from cache')
            return cache.readCache(fileName)

class Cache:
    def __init__(self, fileName:str):
        self.fileName = fileName

    def isCached(self, fileName:str):
        return path.exists(fileName)

    def writeCache(self,fileName:str, data):
        if not path.exists(cacheFolder):
            mkdir(cacheFolder,755)
        with open(fileName, 'w+') as outputfile:
            json.dump(data,outputfile)

    def readCache(self, fileName:str):
        with open(fileName) as jsonfile:
            return unpackJson(json.load(jsonfile))
