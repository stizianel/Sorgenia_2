'''
Created on 17/apr/2013

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
log = LogManager('u_zever', Constants.getDebugMode(),date,htmlMode)
#creazione oggetto di connessione Oracle
conn = ConnectionManager('u_zever',log)
#inizializzazione e apertura file CSV
mycsv = CsvManager('u_zever',';',False)
#nome programma
log.testata("aggiornamento ZEVER" )

cursor = conn.conn.cursor()
cur_s1 = conn.conn.cursor()
cursor.execute("ALTER SESSION SET NLS_DATE_FORMAT = 'YYYYMMDD HH24:MI:SS'")
#
sap_conn=pysap.Rfc_connection(conn_file='sapconn.ini',conn_name='IAQ')
sap_conn.open()
#
campi_temksv = ['vertrag', 'vkonto', 'anlage', 'gsber', 'vrefer', 'einzdat', 'auszdat']
#
M=[]
conta=0
tota=0
cursor.execute("TRUNCATE TABLE Z_EVER");
cursor.execute("COMMIT")
log.writeInfo("Inizio estrazione da SAP")
ITBOLT = sap_conn.read_table('EVER',fields=campi_temksv,max_rows=800000)
log.writeInfo("Fine estrazione da SAP estratti " + str(ITBOLT.count)) 
for row in ITBOLT:
    
    w_vertrag = str(row.vertrag)[-10:]
    w_vkonto = str(row.vkonto)[-12:]
    w_anlage = str(row.anlage)[-10:]
    w_gsber = str(row.gsber)[-4:]
    w_vrefer = str(row.vrefer)[-20:]
    w_einzdat = str(row.einzdat)[-8:]
    w_auszdat = str(row.auszdat)[-8:]
    
    M.append((w_vertrag, w_vkonto, w_anlage, w_gsber, w_vrefer, w_einzdat, w_auszdat))
    conta = conta + 1
    if conta == 10000:    
        cursor.prepare("INSERT INTO Z_EVER(vertrag, vkonto, anlage, gsber, vrefer, einzdat, auszdat) VALUES (:1, :2, :3, :4, :5, :6, :7)")
        cursor.executemany(None, M)
        cursor.execute("COMMIT")
        tota = tota + conta
        conta = 0
        M=[]
        log.writeInfo("elaborati " + str(tota) + " records")
#
cursor.prepare("INSERT INTO Z_EVER(vertrag, vkonto, anlage, gsber, vrefer, einzdat, auszdat) VALUES (:1, :2, :3, :4, :5, :6, :7)")
cursor.executemany(None, M)
cursor.execute("COMMIT")
tota = tota + conta
log.writeInfo("elaborati " + str(tota) + " records")
cur_s1.close()
cursor.close()
conn.closeConnection()
log.close()