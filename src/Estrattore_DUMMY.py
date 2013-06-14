#-*- coding: latin-1 -*-
'''
Creato da Manfredini Marco

Azienda: Eutile
'''

import datetime
from it_eutile_utils_extractor.ExtractorManager import ExtractorManager

from it_eutile_utils_aggregator.AggregatorManager import AggregatorManagerExMny


AggregatorManagerExMny('movein_aggregator',1000,'moveinAggregator', filename='movein.xml')
ExtractorManager('movein','moveinExtractor',filename='movein.xml',maxRows=10000) 
