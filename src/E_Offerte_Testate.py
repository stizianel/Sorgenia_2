'''
Created on 09/apr/2013

@author: Stefano Tizianel
'''
import datetime
import csv
from it_eutile_utils_properties.Constants import Constants
#from it_eutile_utils_database.ConnectionManager import ConnectionManager
from it_eutile_utils_log.LogManager import LogManager
from it_eutile_utils_csvmanager.CsvManager import CsvManager
#
import cx_Oracle

connstr = "SAP_USER" + '/' + "sap_user" + '@' + "192.168.0.177" + ':' + "1521" + '/' + "SINPROD"
conn = cx_Oracle.connect(connstr)

stat_finale = '''
 SELECT                                                                                                 
COD_PROPOSTA                                              
,COD_AGENZIA                                               
,COD_AGENTE                                                
,SOCIETA_VENDITA                                           
,DIPENDENTE_RESPONSABILE                                   
,REFERENTE_CONTRATTUALE                                    
,REFERENTE_CONTABILE                                       
,VENDITORE_USCENTE                                         
,COD_CLIENTE                                               
,COD_CONTO_CONTRATTUALE                                    
,TIPOLOGIA_CONTRATTO                                       
,CANALE                                                    
,SERVIZIO                                                  
,FLAG_CCQ                                                  
,FLAG_AGEV_ESEN                                            
,to_char(DATA_FIRMA, 'yyyymmddhh24miss')                   
,to_char(DATA_ACCETTAZIONE, 'yyyymmddhh24miss')            
,to_char(DATA_CCQ, 'yyyymmddhh24miss')                     
,to_char(DATA_CARICAMENTO, 'yyyymmddhh24miss')             
,to_char(DATA_INVIO_CONTR_TSELLER, 'yyyymmddhh24miss')     
,to_char(DATA_INVIO_PRE_BENV, 'yyyymmddhh24miss')          
,to_char(DATA_CREAZIONE_OFFERTA, 'yyyymmddhh24miss')       
,to_char(DATA_ESITO_RIASCOLTO, 'yyyymmddhh24miss')         
,ESITO_RIASCOLTO                                           
,FLAG_ESITO_RIASCOLTO                                      
,STATO_OFFERTA                                             
,MOTIVO_SOSP_RIF                                           
,FLAG_SWITCH_VOLTURA                                       
,NOME_INTEST                                               
,COGNOME_INTEST                                            
,CODICE_FISCALE                                            
,RAGIONE_SOCIALE                                           
,PARTITA_IVA                                               
,ASSOCIAZIONE_CONSORZIO                                    
,CAMPAGNA                                                  
,UFFICIO                                                   
FROM DBI_USER.IFC_SAP_CRM_OFF_TESTATA o, Z_TEMKSV z
where o.cod_cliente = z.oldkey and z.object = 'PARTNER'      
'''
#inizializzazione e apertura file di log
date=datetime.datetime.now()
htmlMode=''
log = LogManager('E_Offerte_Testata', Constants.getDebugMode(),date,htmlMode)
#creazione oggetto di connessione Oracle
#conn = ConnectionManager('E_Sr',log)
#inizializzazione e apertura file CSV
mycsv = CsvManager('offerte_testate',';',False)
#nome programma
#log.testata("creazione csv SR" )

#cursor = conn.conn.cursor()
cur_s1 = conn.cursor()
cur_s1.execute("ALTER SESSION SET NLS_DATE_FORMAT = 'YYYYMMDD'")
cur_s1.execute("ALTER SESSION SET NLS_TIMESTAMP_FORMAT = 'YYYYMMDDHH24MISS'")
#cur_s1.execute("ALTER SESSION SET NLS_TIME_FORMAT = 'HHMMSS'")
cur_s1.execute("SELECT * FROM v$nls_parameters WHERE REGEXP_LIKE(parameter, 'NLS_(DATE|TIME).*')")
for rec_s1 in cur_s1:
                    print("PARAMETER: " + rec_s1[0] + " VALUE: " + rec_s1[1])
#select principale
cur_s1.execute(stat_finale)

i=0      
ifx = '\t'
#loop sul resultset
linesToWrite = []
yy=1
ctrEnde=0
ctrTota=0
with open(mycsv.csvFileName.replace('$s',str(yy)), 'wb') as f:
    csv.register_dialect('csv', delimiter=';',quotechar="'", quoting=csv.QUOTE_MINIMAL)
    dialect = csv.get_dialect('csv')
    writer = csv.writer(f,dialect)
    
    for record_s1 in cur_s1:
        #print record_s1
        w_key = record_s1[0]
        record_l1 = list(record_s1)
        #del record_l1[-1]
        linesToWrite.append(record_l1)
        ctrTota+=1
    writer.writerows(linesToWrite)
    linesToWrite=[]
#chiusura componenti
cur_s1.close()
#cursor.close()
print "Sono state scritte ",ctrTota," righe."
conn.close()
log.close()