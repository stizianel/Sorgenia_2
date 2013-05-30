'''
Created on 11/ott/2012


'''
from it_eutile_utils_aggregator.AggregatorManager import AggregatorManagerExMny
from it_eutile_utils_aggregator.AggregatorManager import AggregatorManagerExecuteProcedure


AggregatorManagerExMny('billdoc_erch_aggregator',100,'billdoc_ERCH_Aggregator', filename='billdocG.xml')
AggregatorManagerExMny('billdoc_erchp_aggregator',100,'billdoc_ERCHP_Aggregator', filename='billdocG.xml')
AggregatorManagerExMny('billdoc_erchz_aggregator',100,'billdoc_ERCHZ_Aggregator', filename='billdocG.xml')
AggregatorManagerExecuteProcedure('billdoc_erchz_prepare',100,'billdoc_ERCHZ_Prepare', filename='billdocG.xml')
AggregatorManagerExMny('billdoc_erdtax_aggregator',100,'billdoc_ERDTAX_Aggregator', filename='billdocG.xml')
