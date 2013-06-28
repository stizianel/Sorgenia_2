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
SELECT
    Tipo_Contatto ,
    Id_Interazione_As_Is ,
    Canale ,
    Direzione ,
    Descrizione ,
    Numero_Operazione ,
    Tipo_Richiedente ,
    User_Id_Creatore ,
    Esito ,
    Partner_Contatto ,
    Dipendente_Responsabile ,
    Gruppo_Responsabile ,
    POD ,
    Pdr ,
    Categoria_1 ,
    Categoria_2 ,
    Categoria_3 ,
    Numero_Documenti ,
    TO_CHAR(Data_Apertura,'yyyymmddhh24miss') ,
    TO_CHAR(Data_Chiusura,'yyyymmddhh24miss') ,
    TO_CHAR(Data_Ricezione_Richiesta,'yyyymmddhh24miss') ,
    Identificativo_Opt ,
    Note ,
    Note2 ,
    Note3 ,
    CA ,
    TO_CHAR(Data_Invio,'yyyymmddhh24miss') ,
    Tipo_Corrispondenza ,
    Genere_Corrispondenza ,
    Altri_Destinatari
FROM
    dbi_user.IFC_SAP_CRM_INT_CONTATTI,
    sapsr3.but000@sap_caq b, --partner
    sapsr3.isu_pod@sap_caq c, --ext_ui
    sapsr3.crmm_babr_h@sap_caq d --zzvkona
WHERE
    lpad(Partner_Contatto,10,'0') = lpad(b.partner,10,'0')
AND pod = c.ext_ui
AND d.zzvkona = ca
AND Categoria_3 NOT IN ('TBD',
                        'N.A.')
AND Categoria_3 IS NOT NULL      
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