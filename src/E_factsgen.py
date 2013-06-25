'''
Created on 07/nov/2012

@author: stefano.tizianel
'''
import datetime
import csv
from it_eutile_utils_properties.Constants import Constants
from it_eutile_utils_csvmanager.CsvManager import CsvManager
from it_eutile_utils_database.ConnectionManager import ConnectionManager
from it_eutile_utils_log.LogManager import LogManager
#-----------------------------------------------------------------
mainSelect="select * from facts_key"
lfacts=[("select legacy, tipo, operand, prog                       from facts_f_dema a      where a.legacy = :key group by legacy,tipo,operand,prog ", "select legacy, tipo, ab, bis, lmenge      from facts_v_dema a       where a.legacy = :key and a.prog = :prog and bis >'20080401'"),
        ("select legacy, tipo, operand, ' ', timbasis, timtyp, prog from facts_f_tqua a      where a.legacy = :key group by legacy, tipo, operand, ' ', timbasis, timtyp, prog", "select legacy, tipo, ab, bis, menge, tarifart, kondigr from facts_v_tqua a where a.legacy = :key and a.prog = :prog and bis >'20080401'"),
        ("select legacy, tipo, operand, prog                        from facts_f_qprice a    where a.legacy = :key group by legacy,tipo,operand,prog", "select legacy, tipo, ab, bis, preis,    prsbtr,   waers,    tarifart, kondgir            from facts_v_qprice a     where a.legacy = :key and a.prog = :prog and bis >'20080401'"),
        ("select legacy, tipo, operand, prog                        from facts_f_factor a    where a.legacy = :key group by legacy,tipo,operand,prog" , "select legacy, tipo, ab, bis, factor,   tarifart, kondigr                                from facts_v_factor a     where a.legacy = :key and a.prog = :prog and bis >'20080401'AND BIS>=AB"),
        ("select legacy, tipo, operand, prog                        from facts_f_flag   a    where a.legacy = :key group by legacy,tipo,operand, prog" , "select legacy, tipo, ab, bis, boolkz,   tarifart, kondigr                                from facts_v_flag a       where a.legacy = :key and a.prog = :prog and bis >'20080401'"),
        ("select legacy, tipo, operand, prog                        from facts_f_rate_type a where a.legacy = :key group by legacy, tipo, operand, prog", "select legacy, tipo, ab, bis, tarifart, kondigr     from facts_v_rate_type a  where a.legacy = :key and a.prog = :prog and bis >'20080401'"),
        ("select legacy, tipo, operand, prog                        from facts_f_lpri   a    where a.legacy = :key group by legacy, tipo, operand, prog", "select legacy, tipo, ab, bis, preis, tarifart, kondgir                                   from facts_v_lprice a     where a.legacy = :key and a.prog = :prog and bis >'20080401'"),
        ("select legacy, tipo, operand, prog                        from facts_f_tpri   a    where a.legacy = :key group by legacy, tipo, operand, prog", "select legacy, tipo, ab, bis, preis,    prsbtr,   waers,    tarifart, kondgir            from facts_v_tprice a     where a.legacy = :key and a.prog = :prog and bis >'20080401'"),
        ("select legacy, tipo, operand, prog                        from facts_f_udef   a    where a.legacy = :key group by legacy,tipo,operand,prog", "select legacy, tipo, ab, bis, udefval1, udefval2, udefval3, udefval4, tarifart, kondgir  from facts_v_udef a       where a.legacy = :key and a.prog = :prog and bis >'20080401'")]
date=datetime.datetime.now()
htmlMode=''
#-----------------------------------------------------------------
#  
#inizializzazione e apertura file di log
log = LogManager('factsgen', Constants.getDebugMode(),date,htmlMode)
#                
#inizializzazione e apertura file emigall
mycsv = CsvManager('factsgen','\t',False)
            
#creazione oggetto di connessione Oracle
conn = ConnectionManager('factsgen',log)

#nome programma
log.testata(" creazione csv Emigall " + 'factsgen')

#cursori
cur_s1 = conn.conn.cursor()
cur_s2 = conn.conn.cursor()
cur_s3 = conn.conn.cursor()
#select principale
cur_s1.execute(mainSelect)

i=0      
ifx = '\t'
#loop sul resultset
linesToWrite = []
yy=1
ctrEnde=0
ctrTota=0
with open(mycsv.csvFileName.replace('$s',str(yy)), 'wb') as f:
    csv.register_dialect('emigall', delimiter='\t',quotechar="", quoting=csv.QUOTE_NONE)
    dialect = csv.get_dialect('emigall')
    writer = csv.writer(f,dialect)
                
    for record_s1 in cur_s1:
#        print record_s1
        w_key = record_s1[0]
        linesToWrite.append(record_s1)
        ctrTota+=1
#        print "record_s1: ", record_s1
        for select, select2 in lfacts:
            cur_s2.execute(select,key=w_key)
            for record_s2 in cur_s2:
                w_prog = record_s2[-1]
                #linesToWrite.append(record_s2) questa istruzione stampa anche l'ultimo campo W_PROG
                linesToWrite.append(record_s2[0: len(record_s2) -1]) #niente ultimo campo W_PROG
                ctrTota+=1
#                print "  record_s2 full: ", record_s2
#                print "  record_s2     : ", record_s2[0: len(record_s2) -1]
                cur_s3.execute(select2, key=w_key, prog=w_prog)
                for record_s3 in cur_s3:
                    linesToWrite.append(record_s3)
                    ctrTota+=1
#                    print "    record_s3 full: ", record_s3
        ultima = (w_key, '&ENDE')
        linesToWrite.append(ultima)
        ctrEnde+=1
    writer.writerows(linesToWrite)
    linesToWrite=[]
                    
#chiusura componenti
cur_s1.close()
cur_s2.close()
print "Sono state scritte ",ctrEnde," strutture e per un totale di ",ctrTota," righe."
conn.closeConnection()
log.close()