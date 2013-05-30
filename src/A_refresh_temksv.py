'''
Created on 16/nov/2012

@author: Stizianel
'''
import datetime
import pysap
from it_eutile_utils_properties.Constants import Constants
from it_eutile_utils_database.ConnectionManager import ConnectionManager
from it_eutile_utils_log.LogManager import LogManager
#-----------------------------------------------------------------
#
date=datetime.datetime.now()
htmlMode=''
#inizializzazione e apertura file di log
log = LogManager('ref_temksv', Constants.getDebugMode(),date,htmlMode)
#
#creazione oggetto di connessione Oracle
conn = ConnectionManager('ref_temksv',log)
cursor = conn.conn.cursor()
cursor.execute("ALTER SESSION SET NLS_DATE_FORMAT = 'YYYYMMDD HH24:MI:SS'")
#
w_options="object='PARTNER'"
sap_conn=pysap.Rfc_connection(conn_file='sapconn.ini',conn_name='INT1')
sap_conn.open()
sql = "INSERT INTO Z_TEMKSV ("
ITBOLT = sap_conn.read_table('TEMKSV', options=["object = 'PARTNER'"], max_rows=200000)
for row in ITBOLT:
    rigad=row.to_dict()
    del rigad['mandt']
    campi = rigad.keys()
    campi_s = ",".join(campi)
    valori = rigad.values()
    valori_s = valori.__str__()
    valori_s1 = valori_s.replace('[','')
    valori_s2 = valori_s1.replace(']','')
    sqls = sql + campi_s + ") values (" + valori_s2 + ")"
    print "stringasql ", sqls
    cursor.execute(sqls)
cursor.execute("COMMIT")

    