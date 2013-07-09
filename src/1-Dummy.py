#-*- coding: latin-1 -*-
'''
Creato da Manfredini Marco

Azienda: Eutile
'''

import datetime
from it_eutile_utils_extractor.ExtractorManager import ExtractorManager
from it_eutile_utils_aggregator.AggregatorManager import AggregatorManagerExMny
from it_eutile_utils_aggregator.AggregatorManager import AggregatorManagerExecuteProcedure


AggregatorManagerExMny('partnerAggregatorBase',1000,'partnerAggregatorBase',filename='partner_referente.xml') 
ExtractorManager('partner_referente','partnerRefExtractor',filename='partner_referente.xml')


