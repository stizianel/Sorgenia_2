'''
Created on 10/10/2012


'''
from it_eutile_utils_extractor.ExtractorManager import ExtractorManager
#from it_eutile_utils_aggregator.AggregatorManager import AggregatorManagerExMny

#la parte preExtractor non serve piu' in quanto gestita nel processo di aggregazione
#AggregatorManagerExMny('preExtractor',1000,'preExtractor', filename='test.xml')
ExtractorManager('billdoc33','billdocExtractor', filename='billdoc21.xml') 

