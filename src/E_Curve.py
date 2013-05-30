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
SELECT pod, tipo, Start_Date, Start_Ts, Start_Offset, End_Date, End_Ts, End_Offset, Misura, Filler, Um, Spazio from ( 
     select         r.pod as pod,
                     'EDM_ATTIVA' as tipo,
                     -- Versione max  
                     --Sb.offset  Initial_Offset,  -- Ottengo l'offset della data di inizio periodo
                     --Se.offset  Final_Offset,     -- Ottengo l'offset della data di fine periodo
                     TO_CHAR(m.Dt_Utc + (Sb.Offset/24), 'YYYYMMDD')  Start_Date,
                     TO_CHAR(m.Dt_Utc + (Sb.Offset/24), 'HH24MISS')  Start_Ts,
                     '+' || TRIM(TO_CHAR(Sb.offset, '00')) Start_Offset,
                     TO_CHAR(m.Dt_Utc + (15 / (24 * 60))+ (Se.Offset/24), 'YYYYMMDD')  End_Date,
                     TO_CHAR(m.Dt_Utc + (15 / (24 * 60))+ (Se.Offset/24), 'HH24MISS')  End_Ts,
                     '+' || TRIM(TO_CHAR(Se.offset, '00')) End_Offset,
                     m.n_ener_attiva as Misura,
                     '00' as Filler, 
                     'KWH' as Um,
                     ' ' as Spazio,
                     to_char(m.Dt_Utc + (Sb.Offset/24), 'YYYYMM')||'EDM_ATTIVA' as ordine,
                     dt_utc as utc
                from dbi_user.rpl_anu_t_misure_ee_hh  m,
                     dbi_user.ifc_sap_punti_fornitura r,
                     instmgmt_diint                   i,
                     dbi_user.Ifc_Sap_Daylight_Saving sb,   -- Per trovare l'offset dell'inizio periodo
                     dbi_user.Ifc_Sap_Daylight_Saving se    -- Per trovare l'offset della fine periodo
               where m.id_tp_misura = 6
                 and m.cd_punto = 'PR19771'
                 and m.cd_punto = i.anlage
                 and m.cd_punto = r.dbi_cd_punto
                 and r.ordine_reverse = 1
                 and m.fl_completa = 'S'
                 and m.dt_mese_competenza >= to_date(eadat, 'yyyymmdd') --, TO_DATE('01032012', 'DDMMYYYY'))
                 AND sb.Utc_begin <= dt_Utc
                 AND sb.Utc_End > Dt_Utc
                 AND se.Utc_begin <= (dt_utc + (15 / (24 * 60)))
                 AND se.Utc_End > (dt_Utc + (15 / (24 * 60)))
                -- and to_char(dt_timestamp, 'yyyymmdd') IN  ('20121028', '20120325', '20120324')
      union all
                select r.pod,
                     'EDM_REATTIVA',
                     -- Versione max  
                     --Sb.offset  Initial_Offset,  -- Ottengo l'offset della data di inizio periodo
                     --Se.offset  Final_Offset,     -- Ottengo l'offset della data di fine periodo
                     TO_CHAR(m.Dt_Utc + (Sb.Offset/24), 'YYYYMMDD')  Start_Date,
                     TO_CHAR(m.Dt_Utc + (Sb.Offset/24), 'HH24MISS')  Start_Ts,
                     '+' || TRIM(TO_CHAR(Sb.offset, '00')) Start_Offset,
                     TO_CHAR(m.Dt_Utc + (15 / (24 * 60))+ (Se.Offset/24), 'YYYYMMDD')  End_Date,
                     TO_CHAR(m.Dt_Utc + (15 / (24 * 60))+ (Se.Offset/24), 'HH24MISS')  End_Ts,
                     '+' || TRIM(TO_CHAR(Se.offset, '00')) End_Offset,
                     m.n_ener_reatt,
                     '00',
                     'KRH',
                     ' ',
                     to_char(m.Dt_Utc + (Sb.Offset/24), 'YYYYMM')||'EDM_REATTIVA' as ordine,
                     dt_utc as utc
                from dbi_user.rpl_anu_t_misure_ee_hh  m,
                     dbi_user.ifc_sap_punti_fornitura r,
                     instmgmt_diint                   i,
                     dbi_user.Ifc_Sap_Daylight_Saving sb,   -- Per trovare l'offset dell'inizio periodo
                     dbi_user.Ifc_Sap_Daylight_Saving se    -- Per trovare l'offset della fine periodo
               where m.id_tp_misura = 6
                 and m.cd_punto = 'PR19771'
                 and m.cd_punto = i.anlage
                 and m.cd_punto = r.dbi_cd_punto
                 and r.ordine_reverse = 1
                 and m.fl_completa = 'S'
                 and m.dt_mese_competenza >= to_date(eadat, 'yyyymmdd') --, TO_DATE('01032012', 'DDMMYYYY'))
                 AND sb.Utc_begin <= dt_Utc
                 AND sb.Utc_End > Dt_Utc
                 AND se.Utc_begin <= (dt_utc + (15 / (24 * 60)))
                 AND se.Utc_End > (dt_Utc + (15 / (24 * 60)))
                 )
                 group by pod, tipo, Start_Date, Start_Ts, Start_Offset, End_Date, End_Ts, End_Offset, Misura, Filler, Um, Spazio, ordine, utc
                 order by ordine, utc
'''
#inizializzazione e apertura file di log
date=datetime.datetime.now()
htmlMode=''
log = LogManager('E_curve', Constants.getDebugMode(),date,htmlMode)
#creazione oggetto di connessione Oracle
conn = ConnectionManager('E_curve',log)
#inizializzazione e apertura file CSV
mycsv = CsvManager('curve',';',False)
#nome programma
log.testata("creazione csv Curve" )

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
    csv.register_dialect('csv', delimiter=';',quotechar="", quoting=csv.QUOTE_NONE)
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