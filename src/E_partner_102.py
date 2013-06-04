'''
Created on 07/mag/2012
commento di prova
@author: Stefano Tizianel.
'''
from it_eutile_utils_extractor.ExtractorManager import ExtractorManager

#ExtractorManager('partner','partnerExtractor', filename='partner.xml') 
ExtractorManager('partner_referente','partnerRefExtractor',filename='partner_referente.xml',legacyValues ='None',htmlMode='False',maxRows=200000,dblog='False')
ExtractorManager('partner_relazioni','partnerRelExtractor',filename='partner_referente.xml',legacyValues ='None',htmlMode='False',maxRows=200000,dblog='False')

