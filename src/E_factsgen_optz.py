'''
Created on 07/nov/2012

@author: fabio.foti
'''

import datetime
import csv
from it_eutile_utils_properties.Constants import Constants
from it_eutile_utils_csvmanager.CsvManager import CsvManager
from it_eutile_utils_database.ConnectionManager import ConnectionManager
from it_eutile_utils_log.LogManager import LogManager
from threading import Thread
#-----------------------------------------------------------------


#-----------------------------------------------------------------
#
class FactsGenOptz(object):
    def __init__(self,w_lista_gruppo=[("1"),("2"),("3"),("4"),("5"),("6"),("7"),("8"),("9"),("10"),("11"),("12")]):
        threads = []        
        for w_gruppo in w_lista_gruppo:
            factsGenT = Thread(target=runSingleExtractor, args=(self,w_gruppo))    
            factsGenT.setName('factsgen_'+w_gruppo)
            factsGenT.start()
            threads.append(factsGenT)
        threadAlive = True
        while threadAlive:
            threadAlive = False
            for t in threads:
                if t.isAlive():
                    threadAlive = True
        print "Esecuzione Terminata"


    #inizializzazione e apertura file di log
def runSingleExtractor(self,w_gruppo=1):
    mainMasterSelect = "SELECT k.legacy,a.tipo,a.prog,k.legacy||'\t'||k.tipo||'\t'||k.anlage||'\t'||k.bis,a.intestazione,a.dettaglio FROM (select '01F_DEMA' tipo,a.prog prog ,a.legacy||'\t'||a.tipo||'\t'||a.operand intestazione ,b.legacy||'\t'||b.tipo||'\t'||b.ab||'\t'||b.bis||'\t'||b.lmenge dettaglio,a.legacy  from facts_f_dema a,facts_v_dema b where a.legacy = b.legacy and a.prog = b.prog and b.bis >'20080401' group by '01F_DEMA' ,a.prog ,a.legacy||'\t'||a.tipo||'\t'||a.operand ,b.legacy||'\t'||b.tipo||'\t'||b.ab||'\t'||b.bis||'\t'||b.lmenge,a.legacy UNION ALL select '02F_TQUA',A.PROG PROG, A.legacy||'\t'||A.tipo||'\t'||A.operand||'\t'||' '||'\t'||A.timbasis||'\t'||A.timtyp intestazione , B.legacy||'\t'||B.tipo||'\t'||B.ab||'\t'||B.bis||'\t'||B.menge||'\t'||B.tarifart||'\t'||B.kondigr dettaglio,a.legacy from facts_f_tqua a, facts_v_tqua B where a.legacy = B.legacy and a.prog = B.prog and B.bis >'20080401' group by '02F_TQUA',A.PROG , A.legacy||'\t'||A.tipo||'\t'||A.operand||'\t'||' '||'\t'||A.timbasis||'\t'||A.timtyp , B.legacy||'\t'||B.tipo||'\t'||B.ab||'\t'||B.bis||'\t'||B.menge||'\t'||B.tarifart||'\t'||B.kondigr,a.legacy  UNION ALL select '03F_QPRICE' tipo ,a.prog prog ,a.legacy||'\t'||a.tipo||'\t'||a.operand intestazione ,b.legacy||'\t'||b.tipo||'\t'||b.ab||'\t'||b.bis||'\t'||b.preis||'\t'||b.prsbtr||'\t'||b.waers||'\t'||b.tarifart||'\t'||b.kondgir dettaglio,a.legacy from facts_f_qprice a, facts_v_qprice b where a.operand !='ESQP_01_FT' and a.legacy = b.legacy and a.prog = b.prog and b.prog !='126' and b.bis >'20080401' group by '03F_QPRICE',a.prog,a.legacy||'\t'||a.tipo||'\t'||a.operand,b.legacy||'\t'||b.tipo||'\t'||b.ab||'\t'||b.bis||'\t'||b.preis||'\t'||b.prsbtr||'\t'||b.waers||'\t'||b.tarifart||'\t'||b.kondgir,a.legacy UNION ALL select '04F_FACTOR' tipo,a.prog prog, A.legacy||'\t'||A.tipo||'\t'||A.operand intestazione ,B.legacy||'\t'||B.tipo||'\t'||B.ab||'\t'||B.bis||'\t'||B.factor||'\t'||B.tarifart||'\t'||B.kondigr dettaglio,a.legacy from facts_f_factor a,facts_v_factor B "

    mainMasterSelect += " where a.legacy = b.legacy and a.prog = b.prog and b.bis >'20080401' AND b.BIS>=b.AB GROUP BY '04F_FACTOR' ,a.prog , A.legacy||'\t'||A.tipo||'\t'||A.operand,B.legacy||'\t'||B.tipo||'\t'||B.ab||'\t'||B.bis||'\t'||B.factor||'\t'||B.tarifart||'\t'||B.kondigr,a.legacy UNION ALL select '05F_FLAG' tipo,a.prog prog ,a.legacy||'\t'||a.tipo||'\t'||a.operand intestazione ,b.legacy||'\t'||b.tipo||'\t'||b.ab||'\t'||b.bis||'\t'||b.boolkz||'\t'||b.tarifart||'\t'||b.kondigr dettaglio,a.legacy from facts_f_flag   a,facts_v_flag b where a.legacy = b.legacy and b.prog = a.prog and b.bis >'20080401' group by '05F_FLAG' ,a.prog ,a.legacy||'\t'||a.tipo||'\t'||a.operand,b.legacy||'\t'||b.tipo||'\t'||b.ab||'\t'||b.bis||'\t'||b.boolkz||'\t'||b.tarifart||'\t'||b.kondigr,a.legacy UNION ALL select '06F_RATE' tipo,a.prog prog ,A.legacy||'\t'||A.tipo||'\t'||a.operand  intestazione ,b.legacy||'\t'||b.tipo||'\t'||b.ab||'\t'||b.bis||'\t'||b.tarifart||'\t'||b.kondigr dettaglio,a.legacy from facts_f_rate a, facts_v_rate b where a.legacy = b.legacy and a.prog = b.prog and b.bis >'20080401' group by '06F_RATE' ,a.prog ,A.legacy||'\t'||A.tipo||'\t'||a.operand,b.legacy||'\t'||b.tipo||'\t'||b.ab||'\t'||b.bis||'\t'||b.tarifart||'\t'||b.kondigr,a.legacy UNION ALL select '07F_LPRI' tipo,a.prog prog ,a.legacy||'\t'||a.tipo||'\t'||a.operand intestazione ,b.legacy||'\t'||b.tipo||'\t'||b.ab||'\t'||b.bis||'\t'||b.preis||'\t'||b.tarifart||'\t'||b.kondgir dettaglio,a.legacy from facts_f_lpri a,facts_v_lprice b   where a.legacy = b.legacy and a.prog = b.prog and b.bis >'20080401' GROUP BY '07F_LPRI' ,a.prog,a.legacy||'\t'||a.tipo||'\t'||a.operand,b.legacy||'\t'||b.tipo||'\t'||b.ab||'\t'||b.bis||'\t'||b.preis||'\t'||b.tarifart||'\t'||b.kondgir,a.legacy UNION ALL select '08F_TPRI' tipo,a.prog prog ,A.legacy||'\t'||a.tipo||'\t'||a.operand  intestazione ,b.legacy||'\t'||b.tipo||'\t'||b.ab||'\t'||b.bis||'\t'||b.preis||'\t'||b.prsbtr||'\t'||b.waers||'\t'||b.tarifart||'\t'||b.kondgir dettaglio,a.legacy "
    mainMasterSelect +=  " from facts_f_tpri   a, facts_v_tprice b   where a.legacy = b.legacy and a.prog = b.prog and b.bis >'20080401' GROUP BY '08F_TPRI' ,a.prog,A.legacy||'\t'||a.tipo||'\t'||a.operand,b.legacy||'\t'||b.tipo||'\t'||b.ab||'\t'||b.bis||'\t'||b.preis||'\t'||b.prsbtr||'\t'||b.waers||'\t'||b.tarifart, b.kondgir,a.legacy UNION ALL select '09F_UDEF' tipo,a.prog prog ,a.legacy||'\t'||a.tipo||'\t'||a.operand intestazione ,b.legacy||'\t'||b.tipo||'\t'||b.ab||'\t'||b.bis||'\t'||b.udefval1||'\t'||b.udefval2||'\t'||b.udefval3||'\t'||b.udefval4||'\t'||b.tarifart||'\t'||b.kondgir dettaglio,a.legacy from facts_f_udef   a,facts_v_udef b  where a.legacy = b.legacy and a.prog = b.prog and b.bis >'20080401' GROUP BY '09F_UDEF' ,a.prog,a.legacy||'\t'||a.tipo||'\t'||a.operand,b.legacy||'\t'||b.tipo||'\t'||b.ab||'\t'||b.bis||'\t'||b.udefval1||'\t'||b.udefval2||'\t'||b.udefval3||'\t'||b.udefval4||'\t'||b.tarifart||'\t'||b.kondgir,a.legacy " 
    mainMasterSelect +=  " ) a,facts_key k where k.gruppo = :gruppo and a.legacy = k.legacy ORDER BY k.legacy,a.TIPO,a.PROG"

    date=datetime.datetime.now()
    htmlMode=''
    log = LogManager('factsgen_optz_'+w_gruppo, Constants.getDebugMode(),date,htmlMode)
    #                
    #inizializzazione e apertura file emigall
    mycsv = CsvManager('factsgen_optz_'+w_gruppo,'\t',False)
                
    #creazione oggetto di connessione Oracle
    conn = ConnectionManager('factsgen_optz_'+w_gruppo,log)
    
    #nome programma
    log.testata(" creazione csv Emigall " + 'factsgen_optz_'+w_gruppo)
    
    #cursori
    cur_s1 = conn.conn.cursor()
    cur_s2 = conn.conn.cursor()
    #select principale
    cur_s1.execute(mainMasterSelect, gruppo=w_gruppo)
    log.writeInfo("----- Fine Esecuzione Query Gruppo " + w_gruppo + " -----")
    #loop sul resultset
    linesToWrite = []
    yy=1
    ctrEnde=0
    ctrTota=0
    with open(mycsv.csvFileName.replace('$s',str(yy)), 'wb') as f:
        csv.register_dialect('emigall', delimiter='\t',quotechar="", quoting=csv.QUOTE_NONE)
        dialect = csv.get_dialect('emigall')
        writer = csv.writer(f,dialect)
        w_prog_prec = ''
        w_type_prec = '' 
        w_key_prec = ''           
        for record_s1 in cur_s1:
    #        print record_s1
            w_key = record_s1[0]
            w_prog = record_s1[2]
            w_type = record_s1[1]
            if (w_key!=w_key_prec and w_key_prec!=''):
                ultima = (w_key, '&ENDE')
                linesToWrite.append(ultima)
                ctrEnde+=1
            if (w_key!=w_key_prec):
                linesToWrite.append(record_s1[3].split('\t'))
                ctrTota+=1
            if (w_key!=w_key_prec or w_prog!=w_prog_prec or w_type!=w_type_prec):
                linesToWrite.append(record_s1[4].split('\t')) #niente ultimo campo W_PROG
                ctrTota+=1
            linesToWrite.append(record_s1[5].split('\t'))
            ctrTota+=1
            w_type_prec = w_type
            w_prog_prec = w_prog
            w_key_prec = w_key
    
           
            if (ctrEnde % 1000 == 0):
                writer.writerows(linesToWrite)
                linesToWrite = []
        ultima = (w_key_prec, '&ENDE')
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