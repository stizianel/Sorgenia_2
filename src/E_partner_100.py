'''
Created on 31/mag/2012

@author: andrea.rossoni Creanetwork S.r.l.
'''
from it_eutile_utils_extractor.ExtractorManager import ExtractorManager

#ExtractorManager('partner','partnerExtractor', filename='partner.xml') 
ExtractorManager('partner','partnerExtractor',filename='partner.xml',legacyValues ='None',htmlMode='False',maxRows=200000,dblog='False')

