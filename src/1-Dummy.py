#-*- coding: latin-1 -*-
'''
Creato da Manfredini Marco

Azienda: Eutile
'''

import datetime
from it_eutile_utils_extractor.ExtractorManager import ExtractorManager
from it_eutile_utils_aggregator.AggregatorManager import AggregatorManagerExMny
from it_eutile_utils_aggregator.AggregatorManager import AggregatorManagerExecuteProcedure


#AggregatorManagerExMny('DOCU_STORICI_Aggregator',10000,'DOCU_STORICI_Aggregator', filename='billdoc-pistolo.xml')
#AggregatorManagerExMny('billdoc_erch_aggregator',10000,'billdoc_ERCH_Aggregator', filename='billdoc-pistolo.xml')
#AggregatorManagerExMny('billdoc_erch_aggregator2',10000,'billdoc_ERCH_Aggregator2', filename='billdoc-pistolo.xml')
#AggregatorManagerExMny('billdoc_erchp_aggregator',10000,'billdoc_ERCHP_Aggregator', filename='billdoc-pistolo.xml')
#AggregatorManagerExMny('billdoc_erchz_aggregator',10000,'billdoc_ERCHZ_Aggregator', filename='billdoc-pistolo.xml')
#AggregatorManagerExecuteProcedure('billdoc_erchz_prepare',10000,'billdoc_ERCHZ_Prepare', filename='billdoc-pistolo.xml')
#AggregatorManagerExMny('billdoc_erdtax_aggregator',10000,'billdoc_ERDTAX_Aggregator', filename='billdoc-pistolo.xml')
ExtractorManager('billdoc','billdocExtractor', filename='billdoc2.xml') 

