#-*- coding: latin-1 -*-
'''
Creato da Manfredini Marco

Azienda: Eutile
'''

import datetime
from it_eutile_utils_extractor.ExtractorManager import ExtractorManager

from it_eutile_utils_aggregator.AggregatorManager import AggregatorManagerExMny


AggregatorManagerExMny('connobj_aggregator',10000,'connobjAggregator',filename='connobj.xml')
ExtractorManager('connobj','connobjExtractor', filename='connobj.xml',maxRows=100000) 
