#-*- coding: latin-1 -*-
'''
Creato da Manfredini Marco

Azienda: Eutile
'''

import datetime
from it_eutile_utils_extractor.ExtractorManager import ExtractorManager
from it_eutile_utils_aggregator.AggregatorManager import AggregatorManagerExMny
from it_eutile_utils_aggregator.AggregatorManager import AggregatorManagerExecuteProcedure


AggregatorManagerExMny('partnerAggregatorBase',10000,'partnerAggregatorBase', filename='partner.xml')
#AggregatorManagerExMny('billdoc_erch_aggregator2',10000,'billdoc_ERCH_Aggregator2', filename='billdoc.xml')
#AggregatorManagerExMny('billdoc_erchp_aggregator',10000,'billdoc_ERCHP_Aggregator', filename='billdoc.xml')
#AggregatorManagerExMny('billdoc_erchz_aggregator',10000,'billdoc_ERCHZ_Aggregator', filename='billdoc.xml')
#AggregatorManagerExecuteProcedure('billdoc_erchz_prepare',10000,'billdoc_ERCHZ_Prepare', filename='billdoc.xml')
#AggregatorManagerExMny('billdoc_erdtax_aggregator',10000,'billdoc_ERDTAX_Aggregator', filename='billdoc.xml')
#ExtractorManager('billdoc','billdocExtractor', filename='billdoc2.xml') 
#AggregatorManagerExMny('billdocHAggregator',10000,'billdocHAggregator', filename='billdoc_h.xml')
#ExtractorManager('TAPPI_ELE','billdocHExtractor', filename='billdoc_h.xml') 

