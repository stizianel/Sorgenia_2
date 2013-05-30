'''
Created on 01/Oct/2012

@author: Stefano Tizianel E-Utile
'''
from it_eutile_utils_extractor.ExtractorManager import ExtractorManager

ExtractorManager('QpriceExtractor','FactQpriExtractor',filename='facts_qpri_e.xml') 
ExtractorManager('LPriceExtractor','LPriceExtractor',filename='facts_qpri_e.xml') 
ExtractorManager('TPriceExtractor','TPriceExtractor',filename='facts_qpri_e.xml') 

