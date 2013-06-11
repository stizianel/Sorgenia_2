'''
Created on 23/apr/2013

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
select gpart,
       trx_number,
       z2.newkey as document,
       docuemnt_type,
       importo_ceduto,
       data_cessione,
       z3.newkey as payment
  from dbi_user.rpl_oa_xxene_factor_cess_all a, dbi_user.wrk_oa_documents b
  left outer join sapsr3.temksv@sap_iaq z3
    on (z3.oldkey = b.cd_entita_fatt || '-' || B.CUSTOMER_TRX_ID and z3.object = 'PAYMENT'), 
       sapsr3.fkkvkp@sap_iaq p, 
       sapsr3.temksv@sap_iaq z, 
       sapsr3.temksv@sap_iaq z2
 where a.customer_trx_id = b.customer_trx_id
   and b.cd_entita_fatt = z.oldkey
   and z.object = 'ACCOUNT'
   and z2.oldkey = b.cd_entita_fatt || '-' || B.CUSTOMER_TRX_ID
   and z2.object = 'DOCUMENT'
   and z.newkey = p.vkont
'''
#inizializzazione e apertura file di log
date=datetime.datetime.now()
htmlMode=''
log = LogManager('E_FactorPartite', Constants.getDebugMode(),date,htmlMode)
#creazione oggetto di connessione Oracle
conn = ConnectionManager('E_FactorPartite',log)
#inizializzazione e apertura file CSV
mycsv = CsvManager('factorPartite',';',False)
#nome programma
log.testata("creazione csv Partite Factor" )

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