'''
Created on 09/10/2012


'''
from it_eutile_utils_extractor.ExtractorManager import ExtractorManager

ExtractorManager('fact_Dema','FactDemaExtractor', filename='fact_Dema.xml') 
ExtractorManager('Fact_TQua','FactTquaExtractor', filename='facts_quant.xml')
ExtractorManager('FactorExtractor','FactorExtractor',filename='facts_factor.xml') 
ExtractorManager('QpriceExtractor','FactQpriExtractor',filename='facts_qpri_e.xml') 
ExtractorManager('RateExtractor','RateExtractor',filename='facts_rate.xml') 



