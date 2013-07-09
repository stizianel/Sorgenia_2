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
#import cx_Oracle

# connstr = "SAP_USER" + '/' + "sap_user" + '@' + "192.168.0.177" + ':' + "1521" + '/' + "SINPROD"
# conn = cx_Oracle.connect(connstr)

stat_finale = '''
SELECT
    DISTINCT posi.Cod_Proposta ,
    posi.Cod_Conto_Contrattuale ,
    Cod_Prodotto ,
    Mercato_Provenienza ,
    Apparecchiatura ,
    Stato_Pre_Switch ,
    Disalimentabilita ,
    Codice_Remi ,
    Fl_Remi_Non_Cert ,
    Fl_Distr_Non_Cert ,
    TO_CHAR(Data_Invio_Benvenuto,'yyyymmddhh24miss') ,
    TO_CHAR(Data_Inizio_Fornitura,'yyyymmddhh24miss') ,
    TO_CHAR(Data_Fine_Fornitura,'yyyymmddhh24miss') ,
    TO_CHAR(Data_Invio_Reces_Trader,'yyyymmddhh24miss') ,
    TO_CHAR(Data_Creazione_Pratica,'yyyymmddhh24miss') ,
    TO_CHAR(Data_Invio_Pratica,'yyyymmddhh24miss') ,
    Numero_Pratica ,
    posi.Cod_Cliente ,
    Cod_Vendit_Uscente ,
    POD ,
    Distributore_Locale ,
    Cod_Misuratore ,
    Stato_Pos_Offerta ,
    posi.Motivo_Sosp_Rif ,
    IBAN ,
    Zona_Climatica ,
    Classe_Prelievo_AEEG ,
    TO_CHAR(Data_Fine_Fornitura_Prev,'yyyymmddhh24miss') ,
    Volume_Mese ,
    Impegno_Contrattuale ,
    Numero_Pronto_Interv ,
    Numero_Contratto ,
    Consumo_Annuo_Compl ,
    Cod_Versione ,
    Residente ,
    REPLACE(Potenza_Contrattuale,',','.') ,
    REPLACE(Potenza_Disponibile,',','.') ,
    REPLACE(Potenza_Impegnata,',','.') ,
    Tipologia_Uso_Elettr ,
    Livello_Tensione ,
    Tipologia_Uso_Gas ,
    Uso_Gas ,
    Classificazione_Uso ,
    Giorni_Lavorativi ,
    Fatturazione_Mensile ,
    Promozione ,
    Cd_Cliente_Promotore ,
    Cd_Punto_Promotore ,
    Opz_Energia_Pulita ,
    Best_Option_Plan ,
    Premio_Sottoscr ,
    Opz_Last_Call
FROM
    dbi_user.IFC_SAP_CRM_OFF_POSIZIONE posi,
    dbi_user.IFC_SAP_CRM_OFF_TESTATA testa,
    sapsr3.but000@sap_caq b, --partner
    --sapsr3.isu_pod@sap_caq c, --ext_ui
    sapsr3.crmm_babr_h@sap_caq d --zzvkona
    -- Bisogna mettere il codice_proposta associato perche deve legarsi all'offerta
WHERE
    posi.cod_proposta = testa.cod_proposta
    and lpad(posi.cod_cliente,10,'0') = lpad(b.partner,10,'0')
--AND pod = c.ext_ui
AND d.zzvkona = posi.cod_conto_contrattuale 

'''
#inizializzazione e apertura file di log
date=datetime.datetime.now()
htmlMode=''
log = LogManager('E_Offerte_Posizioni', Constants.getDebugMode(),date,htmlMode)
#creazione oggetto di connessione Oracle
conn = ConnectionManager('E_Sr',log)
#inizializzazione e apertura file CSV
mycsv = CsvManager('offerte_posizioni',';',False)
#nome programma
#log.testata("creazione csv SR" )

cursor = conn.conn.cursor()
cur_s1 = conn.conn.cursor()
#cur_s1 = conn.cursor()
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