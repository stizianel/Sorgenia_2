'''
Created on 09/apr/2013

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
select id_interazione_as_is,
       canale,
       direzione,
       descrizione,
       numero_operazione,
       tipo_richiedente,
       user_id_creatore,
       esito,
       partner_contatto,
       dipendente_responsabile,
       gruppo_responsabile,
       pod,
       pdr,
       categoria_1,
       categoria_2,
       categoria_3,
       c.numero_documenti,
       to_char(c.data_apertura, 'YYYYMMDDhh24miss'),
       to_char(c.data_chiusura, 'YYYYMMDDhh24miss'),
       to_char(c.data_ricezione_richiesta, 'YYYYMMDDhh24miss'),
       substr(c.identificativo_opt,0,20),
       substr(c.note,0,999),
       substr(c.note,999,999),
       substr(c.note,1998,999),
       z.newkey,
       to_char(c.data_invio, 'YYYYMMDDhh24miss'),
       c.tipo_corrispondenza,
       c.genere_corrispondenza,
       c.altri_destinatari
  from dbi_user.Ifc_Sap_Crm_Int_Contatti c, z_temksv z, z_temksv z2
  where 
  (z.object = 'ACCOUNT'  and c.ca = z.oldkey)
  and (z2.object = 'PARTNER' and c.partner_contatto = z2.oldkey)
  and length(categoria_1||categoria_2||categoria_3) = 12
  and categoria_1 <> 'N.A.'
  --and rownum < 100001
  group by
        id_interazione_as_is,
       canale,
       direzione,
       descrizione,
       numero_operazione,
       tipo_richiedente,
       user_id_creatore,
       esito,
       partner_contatto,
       dipendente_responsabile,
       gruppo_responsabile,
       pod,
       pdr,
       categoria_1,
       categoria_2,
       categoria_3,
       c.numero_documenti,
       to_char(c.data_apertura, 'YYYYMMDDhh24miss'),
       to_char(c.data_chiusura, 'YYYYMMDDhh24miss'),
       to_char(c.data_ricezione_richiesta, 'YYYYMMDDhh24miss'),
       substr(c.identificativo_opt,0,20),
       substr(c.note,0,999),
       substr(c.note,999,999),
       substr(c.note,1998,999),
       z.newkey,
       to_char(c.data_invio, 'YYYYMMDDhh24miss'),
       c.tipo_corrispondenza,
       c.genere_corrispondenza,
       c.altri_destinatari
      
'''
#inizializzazione e apertura file di log
date=datetime.datetime.now()
htmlMode=''
log = LogManager('E_interazioni', Constants.getDebugMode(),date,htmlMode)
#creazione oggetto di connessione Oracle
conn = ConnectionManager('E_interazioni',log)
#inizializzazione e apertura file CSV
mycsv = CsvManager('interazioni',';',False)
#nome programma
log.testata("creazione csv Interazioni" )

cursor = conn.conn.cursor()
cur_s1 = conn.conn.cursor()
cursor.execute("ALTER SESSION SET NLS_DATE_FORMAT = 'YYYYMMDD HH24:MI:SS'")
#cursor.execute("ALTER SESSION SET NLS_NUMERIC_CHARACTERS = ',.'")
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
        record_l1 = list(record_s1)
        #del record_l1[-1]
        linesToWrite.append(record_l1)
        ctrTota+=1
    writer.writerows(linesToWrite)
    linesToWrite=[]
#chiusura componenti
cur_s1.close()
cursor.close()
print "Sono state scritte ",ctrTota," righe."
conn.closeConnection()
log.close()