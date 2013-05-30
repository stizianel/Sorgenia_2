'''
Created on 15/gen/2013

@author: Stefano Tizianel
'''
import datetime
import pysap
from it_eutile_utils_properties.Constants import Constants
from it_eutile_utils_database.ConnectionManager import ConnectionManager
from it_eutile_utils_log.LogManager import LogManager
from it_eutile_utils_csvmanager.CsvManager import CsvManager
#
#inizializzazione e apertura file di log
date=datetime.datetime.now()
htmlMode=''
log = LogManager('temksv', Constants.getDebugMode(),date,htmlMode)
#creazione oggetto di connessione Oracle
conn = ConnectionManager('E_Temksv',log)
#inizializzazione e apertura file CSV
mycsv = CsvManager('everh',';',False)
#nome programma
log.testata("aggiornamento Temksv" )

cursor = conn.conn.cursor()
cur_s1 = conn.conn.cursor()
cursor.execute("ALTER SESSION SET NLS_DATE_FORMAT = 'YYYYMMDD HH24:MI:SS'")
#
sap_conn=pysap.Rfc_connection(conn_file='sapconn.ini',conn_name='IAQ')
sap_conn.open()
#
campi_temksv = ['mandt', 'firma', 'object','oldkey','newkey']
#
cursor.execute("DELETE FROM Z_TEMKSV WHERE OBJECT = 'ACCOUNTS'")
cursor.execute("COMMIT")
sql1 = "INSERT INTO Z_TEMKSV ("
ITBOLT = sap_conn.read_table('TEMKSV',options=["object = 'ACCOUNTS'"],fields=campi_temksv,max_rows=600000)
for row in ITBOLT:
    rigad=row.to_dict()
    del rigad['mandt']
    campi = rigad.keys()
    campi_s = ",".join(campi)
    valori = rigad.values()
    valori_s = valori.__str__()
    valori_s1 = valori_s.replace('[','')
    valori_s2 = valori_s1.replace(']','')
    sqls = sql1 + campi_s + ") values (" + valori_s2 + ")"
    print "stringasql ", sqls
    cursor.execute(sqls)
cursor.execute("COMMIT")
#
cur_s1.close()
cursor.close()
conn.closeConnection()
log.close()