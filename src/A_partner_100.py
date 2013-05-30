'''
Created on 28/mag/2012

@author: stefano.tizianel
'''
#from it_eutile_utils_aggregator.AggregatorManager import AggregatorManager

from it_eutile_utils_aggregator.AggregatorManager import AggregatorManagerExMny

AggregatorManagerExMny('partner_aggregatorBase',1000,'partnerAggregatorBase', filename='partner.xml')
AggregatorManagerExMny('partner_aggregatorBanche',1000,'partnerAggregatorBanche', filename='partner.xml')
AggregatorManagerExMny('partner_aggregatorIndi',1000,'partnerAggregatorIndi', filename='partner.xml')
AggregatorManagerExMny('partner_aggregatorUtindi',1000,'partnerAggregatorUtindi', filename='partner.xml')
AggregatorManagerExMny('partner_aggregatorTax',1000,'partnerAggregatorTax', filename='partner.xml')

