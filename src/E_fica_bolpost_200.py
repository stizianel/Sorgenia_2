'''
Created on 17/07/2013


'''
from it_eutile_utils_extractor.ExtractorManager import ExtractorManager

#ExtractorManager('document','DocumentExtractor', filename='document.xml')
ExtractorManager('fica_bollettini','BollettiniExtractor', filename='bollettini.xml',legacyValues ='None',htmlMode='False',maxRows=2000000,dblog=False,extractBinaryConsole=False,ende=False,delim=';') 


