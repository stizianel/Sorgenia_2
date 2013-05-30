'''
Created on 04/ott/2012

@author: Creanetwork Srl  Andrea Rossoni
'''
from it_eutile_utils_importer.ImporterManager import ImporterManager
import datetime
ImporterManager('GeolabComuni_Importer',1000,'GeolabComuniImporter',datetime.datetime.now(), filename = 'statements_configurationGEOLAB.xml', input_file_name = 'c:\clienti\SORGENIA_GEOLAB\COMUNI.txt', separator = ';', legacyValues = None, htmlMode = False, fileImport = None, changeFormat = False)