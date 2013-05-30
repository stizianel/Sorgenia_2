'''
Created on 28/mag/2012

@author: stefano.tizianel
         andrea.rossoni Creanetwork S.r.l. 31.5.2012 - deriva da crea_adrcity.py
'''
from it_eutile_utils_aggregator.AggregatorManager import AggregatorManagerExMny

AggregatorManagerExMny('adrcity_aggregator',1000,'adrcityGeolabAggregator', filename='adrcityGeolab.xml') 
AggregatorManagerExMny('adrcitycprt_aggregator',1000,'adrcitycprtGeolabAggregator', filename='adrcityGeolab.xml')
AggregatorManagerExMny('adrcitycpcd_aggregator',1000,'adrcitycpcdGeolabAggregator', filename='adrcityGeolab.xml') 

