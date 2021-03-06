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
mycsv = CsvManager('E_Temksv',';',False)
#nome programma
log.testata("aggiornamento Temksv - MOVE_IN" )

cursor = conn.conn.cursor()
cur_s1 = conn.conn.cursor()
cursor.execute("ALTER SESSION SET NLS_DATE_FORMAT = 'YYYYMMDD HH24:MI:SS'")
#
sap_conn=pysap.Rfc_connection(conn_file='sapconn.ini',conn_name='IAQ')
sap_conn.open()
#
campi_temksv = ['mandt', 'firma', 'object','oldkey','newkey']
#
M=[]
conta=0
tota=0
cursor.execute("DELETE FROM Z_TEMKSV WHERE OBJECT = 'MOVE_IN'");
cursor.execute("COMMIT")
sql1 = "INSERT INTO Z_TEMKSV ("
log.writeInfo("Inizio estrazione da SAP")
ITBOLT = sap_conn.read_table('TEMKSV',options=["object = 'MOVE_IN'"],fields=campi_temksv,max_rows=600000)
log.writeInfo("Fine estrazione da SAP estratti " + str(ITBOLT.count)) 
for row in ITBOLT:
    rigad=row.to_dict()
    del rigad['mandt']
    campi = rigad.keys()
    campi_s = ",".join(campi)
    valori = rigad.values()
    valori_s = valori.__str__()
    valori_s1 = valori_s.replace('[','')
    valori_s2 = valori_s1.replace(']','')
    M.append((valori))
    conta = conta + 1
    if conta == 10000:    
        cursor.prepare("INSERT INTO Z_TEMKSV(firma, oldkey, object, newkey) VALUES (:1, :2, :3, :4)")
        cursor.executemany(None, M)
        cursor.execute("COMMIT")
        tota = tota + conta
        conta = 0
        M=[]
        log.writeInfo("elaborati " + str(tota) + " records")
#
cursor.prepare("INSERT INTO Z_TEMKSV(firma, oldkey, object, newkey) VALUES (:1, :2, :3, :4)")
cursor.executemany(None, M)
cursor.execute("COMMIT")
tota = tota + conta
log.writeInfo("elaborati " + str(tota) + " records")
cur_s1.close()
cursor.close()
conn.closeConnection()
log.close()