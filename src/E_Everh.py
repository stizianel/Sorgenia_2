'''
Created on 15/gen/2013

@author: Stefano Tizianel
'''
import datetime
#import pysap
import csv
from it_eutile_utils_properties.Constants import Constants
from it_eutile_utils_database.ConnectionManager import ConnectionManager
from it_eutile_utils_log.LogManager import LogManager
from it_eutile_utils_csvmanager.CsvManager import CsvManager
#
stat_finale = '''
    SELECT
            vrefer,
            vertrag,
            TO_CHAR(v.d_valido_dal,'yyyymmdd') AS einzdat,
            TO_CHAR(v.d_valido_al,'yyyymmdd')  AS auszdat,
            p.cd_prodotto,
            v.ctar1,
            v.acdan
        FROM
            sapsr3.ever@sap_iap b,
            v_contratti v,
            dbi_user.rpl_anu_t_vers_prodotti c,
            dbi_user.rpl_anu_t_prodotti p
        WHERE
            v.ctar1 = c.cd_versione
        AND c.id_prodotto = p.id_prodotto
        AND b.vrefer = v.cncon
        --AND NOT EXISTS (SELECT 1 FROM sapsr3.everh@sap_iap k WHERE k.vertrag = b.vertrag)
        GROUP BY
            vrefer,
            vertrag,
            TO_CHAR(v.d_valido_dal,'yyyymmdd'),
            TO_CHAR(v.d_valido_al,'yyyymmdd'),
            p.cd_prodotto,
            v.ctar1,
            v.acdan
        ORDER BY
            vrefer desc,
            acdan desc,
            TO_CHAR(v.d_valido_al,'yyyymmdd')
'''
#inizializzazione e apertura file di log
date=datetime.datetime.now()
htmlMode=''
log = LogManager('E_everh', Constants.getDebugMode(),date,htmlMode)
#creazione oggetto di connessione Oracle
conn = ConnectionManager('E_Everh',log)
#inizializzazione e apertura file CSV
mycsv = CsvManager('everh',';',False)
#nome programma
log.testata("creazione csv EVERH" )

cursor = conn.conn.cursor()
cur_s1 = conn.conn.cursor()
cursor.execute("ALTER SESSION SET NLS_DATE_FORMAT = 'YYYYMMDD HH24:MI:SS'")
#
#sap_conn=pysap.Rfc_connection(conn_file='sapconn.ini',conn_name='INT2')
#sap_conn.open()
#
campi_temksv = ['mandt', 'firma', 'object','oldkey','newkey']
#
M=[]
N=[]
#cursor.execute("DELETE FROM Z_TEMKSV WHERE OBJECT = 'MOVE_IN'")
#cursor.execute("COMMIT")
#sql1 = "INSERT INTO Z_TEMKSV ("
#ITBOLT = sap_conn.read_table('TEMKSV',options=["object = 'MOVE_IN'"],fields=campi_temksv,max_rows=600000)
#for row in ITBOLT:
#    rigad=row.to_dict()
#    del rigad['mandt']
#    campi = rigad.keys()
#    campi_s = ",".join(campi)
#    valori = rigad.values()
#    valori_s = valori.__str__()
#    valori_s1 = valori_s.replace('[','')
#    valori_s2 = valori_s1.replace(']','')
#    M.append((valori))
#    #sqls = sql1 + campi_s + ") values (" + valori_s2 + ")"
#    #print "stringasql ", sqls
#    #cursor.execute(sqls)
#cursor.prepare("INSERT INTO Z_TEMKSV(firma, oldkey, object, newkey) VALUES (:1, :2, :3, :4)")
#cursor.executemany(None, M)
#cursor.execute("COMMIT")
#
#campi_ever = ['mandt', 'auszdat', 'vertrag', 'einzdat']
#cursor.execute("TRUNCATE TABLE Z_EVER")
#sql2 = "INSERT INTO Z_EVER ("
#ITBOLT = sap_conn.read_table('EVER',options=["sparte = 'P'"],fields=campi_ever,max_rows=600000)
#for row in ITBOLT:
#    rigad=row.to_dict()
#    del rigad['mandt']
#    campi = rigad.keys()
#    campi_s = ",".join(campi)
#    valori = rigad.values()
#    valori_s = valori.__str__()
#    valori_s1 = valori_s.replace('[','')
#    valori_s2 = valori_s1.replace(']','')
#    N.append((valori))
#    #sqls = sql2 + campi_s + ") values (" + valori_s2 + ")"
#    #print "stringasql ", sqls
#    #cursor.execute(sqls)
#cursor.prepare("INSERT INTO Z_EVER(vertrag, einzdat, auszdat) VALUES (:1, :2, :3)")
#cursor.executemany(None, N)
#cursor.execute("COMMIT")
##cursor.execute("COMMIT")
#
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
    csv.register_dialect('csv', delimiter=';',quotechar="", quoting=csv.QUOTE_NONE)
    dialect = csv.get_dialect('csv')
    writer = csv.writer(f,dialect)
    
    for record_s1 in cur_s1:
    #   print record_s1
        w_key = record_s1[0]
        linesToWrite.append(record_s1)
        ctrTota+=1
    writer.writerows(linesToWrite)
    linesToWrite=[]
#chiusura componenti
cur_s1.close()
cursor.close()
print "Sono state scritte ",ctrTota," righe."
conn.closeConnection()
log.close()