'''
Created on 06/giu/2012

@author: Stefano Tizianel E-Utile
'''
from it_eutile_utils_extractor.ExtractorManager import ExtractorManager

#ExtractorManager('account','accountExtractor', filename='account.xml') 
ExtractorManager('account','accountExtractor',filename='account.xml',legacyValues ='None',htmlMode='False',maxRows=200000,dblog='False')
