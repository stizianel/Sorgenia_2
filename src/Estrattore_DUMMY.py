#-*- coding: latin-1 -*-
'''
Creato da Manfredini Marco

Azienda: Eutile
'''

import datetime
from it_eutile_utils_extractor.ExtractorManager import ExtractorManager

from it_eutile_utils_aggregator.AggregatorManager import AggregatorManagerExMny


AggregatorManagerExMny('accountAggregator',1000,'accountAggregator', filename='account.xml')
ExtractorManager('accountExtractor','accountExtractor',filename='account.xml',maxRows=10000) 
