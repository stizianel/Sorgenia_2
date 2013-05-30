'''
Created on 10/10/2012


'''
from it_eutile_utils_extractor.ExtractorManager import ExtractorManager

#ExtractorManager('payment','PaymentExtractor', filename='payment.xml') 
ExtractorManager('payment','PaymentExtractor',filename='payment.xml',legacyValues ='None',htmlMode='False',maxRows=1000000,dblog='False') 


