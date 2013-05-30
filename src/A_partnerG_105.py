'''
Created on 28/mag/2012

@author: stefano.tizianel
'''
#from it_eutile_utils_aggregator.AggregatorManager import AggregatorManager

from it_eutile_utils_aggregator.AggregatorManager import AggregatorManagerExMny

AggregatorManagerExMny('partner_aggregatorBase',100,'partnerAggregatorBase', filename='partnerG_temp.xml')
AggregatorManagerExMny('partner_aggregatorBanche',100,'partnerAggregatorBanche', filename='partnerG_temp.xml')
AggregatorManagerExMny('partner_aggregatorIndi',100,'partnerAggregatorIndi', filename='partnerG_temp.xml')
AggregatorManagerExMny('partner_aggregatorUtindi',100,'partnerAggregatorUtindi', filename='partnerG_temp.xml')
AggregatorManagerExMny('partner_aggregatorTax',100,'partnerAggregatorTax', filename='partnerG_temp.xml')

