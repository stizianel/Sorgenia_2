'''
Created on 28/mag/2012

@author: stefano.tizianel
         andrea.rossoni Creanetwork S.r.l. 31.5.2012 - deriva da crea_adrcity.py
'''
from it_eutile_utils_aggregator.AggregatorManager import AggregatorManagerExMny

AggregatorManagerExMny('adrcityGeolab_aggregator',    100,'adrcityGeolabAggregator',    filename='adrcityGeolab.xml') 
AggregatorManagerExMny('adrcitycprtGeolab_aggregator',100,'adrcitycprtGeolabAggregator',filename='adrcityGeolab.xml')
AggregatorManagerExMny('adrcitycpcdGeolab_aggregator',100,'adrcitycpcdGeolabAggregator',filename='adrcityGeolab.xml')

