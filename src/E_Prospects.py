'''
Created on 08/apr/2013

@author: Stefano Tizianel
'''
import datetime
import csv
from it_eutile_utils_properties.Constants import Constants
from it_eutile_utils_database.ConnectionManager import ConnectionManager
from it_eutile_utils_log.LogManager import LogManager
from it_eutile_utils_csvmanager.CsvManager import CsvManager
#
stat_finale = '''
select t.anome,
       t.acognome,
       t.arags,
       v.indindi||' '||v.indccvia,
       v.indcivi,
       v.indcap,
       v.inddcom,
       v.indprov,
       decode(v.indnazi, 'ITALIA', 'IT', 'SAN MARINO', 'SM', 'IT'),
       t.anmte,
       acdfi,
       apiva
  from dbi_user.ifc_sap_anagrclienti   t,
       dbi_user.ifc_sap_anagrindirizzi b,
       v_indirizzi                     v
 where b.indcli = t.acdan
   and atipoentita = 'PROSPECT'
   and b.indprog = v.indprog
'''
#inizializzazione e apertura file di log
date=datetime.datetime.now()
htmlMode=''
log = LogManager('E_Prospects', Constants.getDebugMode(),date,htmlMode)
#creazione oggetto di connessione Oracle
conn = ConnectionManager('E_Prospects',log)
#inizializzazione e apertura file CSV
mycsv = CsvManager('prospects',';',False)
#nome programma
log.testata("creazione csv Prospects" )

cursor = conn.conn.cursor()
cur_s1 = conn.conn.cursor()
cursor.execute("ALTER SESSION SET NLS_DATE_FORMAT = 'YYYYMMDD HH24:MI:SS'")
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
    csv.register_dialect('csv', delimiter=';',quotechar="'", quoting=csv.QUOTE_MINIMAL)
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