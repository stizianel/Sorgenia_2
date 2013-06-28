'''
Created on 07/mag/2012
commento di prova
@author: Stefano Tizianel.
'''
import datetime
from it_eutile_utils_extractor.ExtractorManager import ExtractorManager

from it_eutile_utils_aggregator.AggregatorManager import AggregatorManagerExMny
#ExtractorManager('partner','partnerExtractor', filename='partner.xml') 
#AggregatorManagerExMny('partnerAggregatorBase',1000,'partnerAggregatorBase',filename='partner_referente.xml') 
ExtractorManager('partner_referente','partnerRefExtractor',filename='partner_referente.xml',legacyValues ='None',htmlMode='False',maxRows=200000,dblog='False')
ExtractorManager('partner_relazioni','partnerRelExtractor',filename='partner_referente.xml',legacyValues ='None',htmlMode='False',maxRows=200000,dblog='False')


