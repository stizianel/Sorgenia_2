'''
Created on 01/giu/2012

@author: stefano.tizianel
         andrea.rossoni Creanetwork S.r.l. 01.06.2012
         andrea rossoni Creanetwork S.r.l. 25.06.2012
'''
from it_eutile_utils_aggregator.AggregatorManager import AggregatorManagerExMny

AggregatorManagerExMny('adrstreet_aggregator',1000,'adrstreetAggregator', filename='adrstreet.xml')
AggregatorManagerExMny('adrstrpart_aggregator',1000,'adrstrpartAggregator', filename='adrstreet.xml')
AggregatorManagerExMny('adrstrpart2_aggregator',1000,'adrstrpart2Aggregator', filename='adrstreet.xml')