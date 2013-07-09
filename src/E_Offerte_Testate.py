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

# connstr = "SAP_USER" + '/' + "sap_user" + '@' + "192.168.0.177" + ':' + "1521" + '/' + "SINPROD"
# conn = cx_Oracle.connect(connstr)

stat_finale = '''                                                                                          
SELECT
    testa.Cod_Proposta ,
    Cod_Agente ,
    Cod_Agenzia ,
    'Sorgenia S.P.A.' AS Societa_Vendita ,
    Dipendente_Responsabile ,
    Referente_Contrattuale ,
    Intestatario_Contratto ,
    Referente ,
    Referente_Contabile ,
    Venditore_Uscente ,
    testa.Cod_Cliente ,
    testa.Cod_Conto_Contrattuale ,
    Tipologia_Contratto ,
    Canale ,
    Descrizione ,
    Servizio ,
    Flag_CCQ ,
    Flag_Agev_Esen ,
    TO_CHAR(Data_Firma,'yyyymmddhh24miss') ,
    TO_CHAR(Data_Accettazione,'yyyymmddhh24miss') ,
    TO_CHAR(Data_CCQ,'yyyymmddhh24miss') ,
    TO_CHAR(Data_Caricamento,'yyyymmddhh24miss') ,
    TO_CHAR(Data_Invio_Contr_Tseller,'yyyymmddhh24miss') ,
    TO_CHAR(Data_Invio_Pre_Benv,'yyyymmddhh24miss') ,
    TO_CHAR(Data_Creazione_Offerta,'yyyymmddhh24miss') ,
    TO_CHAR(Data_Esito_Riascolto,'yyyymmddhh24miss') ,
    Esito_Riascolto ,
    Flag_Esito_Riascolto ,
    Stato_Offerta ,
    testa.Motivo_Sosp_Rif ,
    Flag_Switch_Voltura ,
    Nome_Intest ,
    Cognome_Intest ,
    Codice_Fiscale ,
    Ragione_Sociale ,
    Partita_IVA ,
    Associazione_Consorzio ,
    Campagna ,
    Ufficio
FROM
    dbi_user.IFC_SAP_CRM_OFF_TESTATA testa,
    dbi_user.IFC_SAP_CRM_OFF_POSIZIONE posi,
    sapsr3.but000@sap_caq b, --partner
    --sapsr3.isu_pod@sap_caq c, --ext_ui
    sapsr3.crmm_babr_h@sap_caq d --zzvkona
WHERE
    lpad(testa.cod_cliente,10,'0') = lpad(b.partner,10,'0')
    --AND pod = c.ext_ui
    and testa.cod_proposta = posi.cod_proposta
AND d.zzvkona = testa.cod_conto_contrattuale   
group by 
testa.Cod_Proposta ,
    Cod_Agente ,
    Cod_Agenzia ,
    'Sorgenia S.P.A.',
    Dipendente_Responsabile ,
    Referente_Contrattuale ,
    Intestatario_Contratto ,
    Referente ,
    Referente_Contabile ,
    Venditore_Uscente ,
    testa.Cod_Cliente ,
    testa.Cod_Conto_Contrattuale ,
    Tipologia_Contratto ,
    Canale ,
    Descrizione ,
    Servizio ,
    Flag_CCQ ,
    Flag_Agev_Esen ,
    TO_CHAR(Data_Firma,'yyyymmddhh24miss') ,
    TO_CHAR(Data_Accettazione,'yyyymmddhh24miss') ,
    TO_CHAR(Data_CCQ,'yyyymmddhh24miss') ,
    TO_CHAR(Data_Caricamento,'yyyymmddhh24miss') ,
    TO_CHAR(Data_Invio_Contr_Tseller,'yyyymmddhh24miss') ,
    TO_CHAR(Data_Invio_Pre_Benv,'yyyymmddhh24miss') ,
    TO_CHAR(Data_Creazione_Offerta,'yyyymmddhh24miss') ,
    TO_CHAR(Data_Esito_Riascolto,'yyyymmddhh24miss') ,
    Esito_Riascolto ,
    Flag_Esito_Riascolto ,
    Stato_Offerta ,
    testa.Motivo_Sosp_Rif ,
    Flag_Switch_Voltura ,
    Nome_Intest ,
    Cognome_Intest ,
    Codice_Fiscale ,
    Ragione_Sociale ,
    Partita_IVA ,
    Associazione_Consorzio ,
    Campagna ,
    Ufficio

'''
#inizializzazione e apertura file di log
date=datetime.datetime.now()
htmlMode=''
log = LogManager('E_Offerte_Testata', Constants.getDebugMode(),date,htmlMode)
#creazione oggetto di connessione Oracle
conn = ConnectionManager('E_Offerte_testata',log)
#inizializzazione e apertura file CSV
mycsv = CsvManager('offerte_testate',';',False)
#nome programma
#log.testata("creazione csv SR" )

cursor = conn.conn.cursor()
cur_s1 = conn.conn.cursor()
cur_s1.execute("ALTER SESSION SET NLS_DATE_FORMAT = 'YYYYMMDD'")
cur_s1.execute("ALTER SESSION SET NLS_TIMESTAMP_FORMAT = 'YYYYMMDDHH24MISS'")
#cur_s1.execute("ALTER SESSION SET NLS_TIME_FORMAT = 'HHMMSS'")
cur_s1.execute("SELECT * FROM v$nls_parameters WHERE REGEXP_LIKE(parameter, 'NLS_(DATE|TIME).*')")
for rec_s1 in cur_s1:
                    print("PARAMETER: " + rec_s1[0] + " VALUE: " + rec_s1[1])
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
        #print record_s1
        w_key = record_s1[0]
        record_l1 = list(record_s1)
        #del record_l1[-1]
        linesToWrite.append(record_l1)
        ctrTota+=1
    writer.writerows(linesToWrite)
    linesToWrite=[]
#chiusura componenti
cur_s1.close()
#cursor.close()
print "Sono state scritte ",ctrTota," righe."
#conn.close()
log.close()