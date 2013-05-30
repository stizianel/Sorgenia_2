'''
Created on 16/apr/2013

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
log = LogManager('u_zfkkvkp', Constants.getDebugMode(),date,htmlMode)
#creazione oggetto di connessione Oracle
conn = ConnectionManager('u_zfkkvkp',log)
#inizializzazione e apertura file CSV
mycsv = CsvManager('u_zfkkvkp',';',False)
#nome programma
log.testata("aggiornamento ZFKKVKP" )

cursor = conn.conn.cursor()
cur_s1 = conn.conn.cursor()
cursor.execute("ALTER SESSION SET NLS_DATE_FORMAT = 'YYYYMMDD HH24:MI:SS'")
#
sap_conn=pysap.Rfc_connection(conn_file='sapconn.ini',conn_name='SDI_VPN')
sap_conn.open()
#
campi_temksv = ['vkont', 'gpart', 'vkbez', 'ktokl']
#
M=[]
conta=0
tota=0
cursor.execute("TRUNCATE TABLE Z_FKKVKP");
cursor.execute("COMMIT")
log.writeInfo("Inizio estrazione da SAP")
#ITBOLT = sap_conn.read_table('FKKVKP',options=["vkont > '003000800001'"],fields=campi_temksv)
ITBOLT = sap_conn.read_table('FKKVKP',fields=campi_temksv)
log.writeInfo("Fine estrazione da SAP estratti " + str(ITBOLT.count)) 
for row in ITBOLT:
    
    w_vkont = str(row.vkont)[-12:]
    w_vkbez = str(row.vkbez)[-35:]
    w_gpart = str(row.gpart)[-10:]
    w_ktokl = str(row.ktokl)[-4:]
    M.append((w_vkont, w_vkbez, w_gpart, w_ktokl))
    conta = conta + 1
    if conta == 10000:    
        cursor.prepare("INSERT INTO Z_FKKVKP(vkont, vkbez, gpart, ktokl) VALUES (:1, :2, :3, :4)")
        cursor.executemany(None, M)
        cursor.execute("COMMIT")
        tota = tota + conta
        conta = 0
        M=[]
        log.writeInfo("elaborati " + str(tota) + " records")
#
cursor.prepare("INSERT INTO Z_FKKVKP(vkont, vkbez, gpart, ktokl) VALUES (:1, :2, :3, :4)")
cursor.executemany(None, M)
cursor.execute("COMMIT")
tota = tota + conta
log.writeInfo("elaborati " + str(tota) + " records")
cur_s1.close()
cursor.close()
conn.closeConnection()
log.close()