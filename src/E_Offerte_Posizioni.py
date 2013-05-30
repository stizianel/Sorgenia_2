'''
Created on 09/apr/2013

@author: Stefano Tizianel
'''
import datetime
import csv
from it_eutile_utils_properties.Constants import Constants
#from it_eutile_utils_database.ConnectionManager import ConnectionManager
from it_eutile_utils_log.LogManager import LogManager
from it_eutile_utils_csvmanager.CsvManager import CsvManager
#
import cx_Oracle

connstr = "SAP_USER" + '/' + "sap_user" + '@' + "192.168.0.177" + ':' + "1521" + '/' + "SINPROD"
conn = cx_Oracle.connect(connstr)

stat_finale = '''
SELECT P.OFFERTE_KEY,
       COD_CONTO_CONTRATTUALE,
       COD_PRODOTTO,
       MERCATO_PROVENIENZA,
       APPARECCHIATURA,
       STATO_PRE_SWITCH,
       DISALIMENTABILITA,
       CODICE_REMI,
       FL_REMI_NON_CERT,
       FL_DISTR_NON_CERT,
       DATA_INVIO_BENVENUTO,
       DATA_INIZIO_FORNITURA,
       DATA_FINE_FORNITURA,
       DATA_INVIO_RECES_TRADER,
       DATA_CREAZIONE_PRATICA,
       DATA_INVIO_PRATICA,
       NUMERO_PRATICA,
       P.COD_CLIENTE,
       COD_VENDIT_USCENTE,
       POD,
       DISTRIBUTORE_LOCALE
       --,CD_PDR
      ,
       STATO_POS_OFFERTA,
       MOTIVO_SOSP_RIF,
       IBAN,
       ZONA_CLIMATICA,
       CLASSE_PRELIEVO_AEEG,
       DATA_FINE_FORNITURA_PREV,
       VOLUME_MESE,
       IMPEGNO_CONTRATTUALE,
       NUMERO_PRONTO_INTERV,
       NUMERO_CONTRATTO,
       CONSUMO_ANNUO_COMPL,
       COD_VERSIONE,
       RESIDENTE,
       POTENZA_CONTRATTUALE,
       POTENZA_DISPONIBILE,
       POTENZA_IMPEGNATA,
       TIPOLOGIA_USO_ELETTR,
       LIVELLO_TENSIONE,
       TIPOLOGIA_USO_GAS,
       USO_GAS,
       CLASSIFICAZIONE_USO,
       GIORNI_LAVORATIVI,
       FATTURAZIONE_MENSILE,
       PROMOZIONE,
       OPZ_ENERGIA_PULITA,
       BEST_OPTION_PLAN,
       PREMIO_SOTTOSCR,
       OPZ_LAST_CALL
  from dbi_user.ifc_sap_crm_off_posizione p,
       dbi_user.ifc_sap_crm_off_prodotti  r,
       z_temksv                           z
 where p.offerte_key = r.offerte_key
   and (p.cod_cliente = z.oldkey and z.object = 'PARTNER')
 group by P.OFFERTE_KEY,
          COD_CONTO_CONTRATTUALE,
          COD_PRODOTTO,
          MERCATO_PROVENIENZA,
          APPARECCHIATURA,
          STATO_PRE_SWITCH,
          DISALIMENTABILITA,
          CODICE_REMI,
          FL_REMI_NON_CERT,
          FL_DISTR_NON_CERT,
          DATA_INVIO_BENVENUTO,
          DATA_INIZIO_FORNITURA,
          DATA_FINE_FORNITURA,
          DATA_INVIO_RECES_TRADER,
          DATA_CREAZIONE_PRATICA,
          DATA_INVIO_PRATICA,
          NUMERO_PRATICA,
          P.COD_CLIENTE,
          COD_VENDIT_USCENTE,
          POD,
          DISTRIBUTORE_LOCALE
          --,CD_PDR
         ,
          STATO_POS_OFFERTA,
          MOTIVO_SOSP_RIF,
          IBAN,
          ZONA_CLIMATICA,
          CLASSE_PRELIEVO_AEEG,
          DATA_FINE_FORNITURA_PREV,
          VOLUME_MESE,
          IMPEGNO_CONTRATTUALE,
          NUMERO_PRONTO_INTERV,
          NUMERO_CONTRATTO,
          CONSUMO_ANNUO_COMPL,
          COD_VERSIONE,
          RESIDENTE,
          POTENZA_CONTRATTUALE,
          POTENZA_DISPONIBILE,
          POTENZA_IMPEGNATA,
          TIPOLOGIA_USO_ELETTR,
          LIVELLO_TENSIONE,
          TIPOLOGIA_USO_GAS,
          USO_GAS,
          CLASSIFICAZIONE_USO,
          GIORNI_LAVORATIVI,
          FATTURAZIONE_MENSILE,
          PROMOZIONE,
          OPZ_ENERGIA_PULITA,
          BEST_OPTION_PLAN,
          PREMIO_SOTTOSCR,
          OPZ_LAST_CALL
'''
#inizializzazione e apertura file di log
date=datetime.datetime.now()
htmlMode=''
log = LogManager('E_Offerte_Posizioni', Constants.getDebugMode(),date,htmlMode)
#creazione oggetto di connessione Oracle
#conn = ConnectionManager('E_Sr',log)
#inizializzazione e apertura file CSV
mycsv = CsvManager('offerte_posizioni',';',False)
#nome programma
#log.testata("creazione csv SR" )

#cursor = conn.conn.cursor()
cur_s1 = conn.cursor()
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
conn.close()
log.close()