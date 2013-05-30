'''
Created on 12/lug/2012

@author: Stefano Tizianel E-Utile
'''
import datetime
from it_eutile_utils_extractor.ExtractorManager import ExtractorManager

ExtractorManager('meterreadExtractor','meterreadExtractor',date = datetime.datetime.now(), filename = 'meterread91.xml', legacyValues = None,htmlMode=False,maxRows=0,dblog=False,extractBinaryConsole=True)
