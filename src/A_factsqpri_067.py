'''
Created on 01/Oct/2012

@author: stefano.tizianel
'''
from it_eutile_utils_aggregator.AggregatorManager import AggregatorManagerExMny

AggregatorManagerExMny('qpri_aggregator',10,'qpriAggregator', filename='facts_qpri_e.xml')
AggregatorManagerExMny('LPriceAggregator',10,'LPriceAggregator', filename='facts_qpri_e.xml')
AggregatorManagerExMny('TPriceAggregator',10,'TPriceAggregator', filename='facts_qpri_e.xml')

