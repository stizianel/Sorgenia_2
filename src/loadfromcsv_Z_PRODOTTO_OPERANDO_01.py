# -*- coding:iso-8859-1 -*-
'''
Created on 22/nov/2012

@author: andrea.rossoni
'''
import cx_Oracle
import csv
from datetime import datetime
import os
import sys

username = os.environ['username']  # x stringa connessione Oracle
password = os.environ['password']  # x stringa connessione Oracle
host     = os.environ['host']      # x stringa connessione Oracle
sid      = os.environ['sid']       # x stringa connessione Oracle
flag     = os.environ['flag']      # C-ompleta (esegue truncate Tabella Z_PRODOTTO_OPERANDO)
                                   # P-arziale 
                                   #   esegue UPDATE se trovata chiave in Tabella Z_PRODOTTO_OPERANDO
                                   #   esegue DELETE se colonna "L"  pari a "D" su Tabella Z_PRODOTTO_OPERANDO
                                   #   esegue INSERT se chiave mancante in Tabella Z_PRODOTTO_OPERANDO
conninfo = username + '/' + password + '@' + host + '/' + sid
print conninfo
#
ctr_I   = 0
ctr_D   = 0
ctr_U   = 0
rigaXls = 0
#connessione al database
try:
    db = cx_Oracle.connect(conninfo)
    print "------------------------------------------------------------"
    print "Benvenuto utente " + username
    print "Sei connesso a Oracle DB versione " + db.version 
    print "------------------------------------------------------------"
except cx_Oracle.DatabaseError, exc:
    error, = exc.args
    print "------------------------------------------------------------"
    print error.message
    print "------------------------------------------------------------"
    sys.exit()
    
cur = db.cursor()
#
prima = 0
#cur.execute("ALTER SESSION SET NLS_DATE_FORMAT = 'YYYYMMDD HH24:MI:SS'")
#print datetime.now()
#
with open('./Modifiche_Facts_04.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        rigaXls+=1
        if (prima == 0):
            prima = 1
            continue    #salto la prima riga nella quale trovo le intestazioni delle colonne
        #
        if ((prima == 1) and (flag == 'C')):
            print "Elaborazione C-ompleta. Pulisco la tabella X_PRODOTTO_OPERANDO...."
            cur.execute("""DELETE FROM Z_PRODOTTO_OPERANDO """)
            cur.execute('COMMIT') 
            prima = 2
        #
        print "-------------------------------------------------------------------------------------- ", str(rigaXls)
        print "PRODOTTO        : ", row[0]
        PRODOTTO                  = row[0]
        #
        print "CTAR1           : ", row[1]
        CTAR1                     = row[1]
        #
        print "UTENZA          : ", row[3]
        UTENZA                    = str(row[3])
        #
        print "ID_OPERANDO     : ", row[4]
        ID_OPERANDO               = str(row[4])
        #
        print "ACQUISIZIONE    : ", row[2]
        ACQUISIZIONE              = str(row[2])
        #
        print "DATA_VALIDITA   : ", row[9]
        DATA_VALIDITA             = str(row[9])
        #
        print "OPERANDO        : ", row[5]
        OPERANDO                  = str(row[5])
        #
        print "TIPO            : ", row[6]
        TIPO                      = str(row[6])
        #
        print "VALORI          : ", row[7]
        VALORI                    = str(row[7])
        #
        print "PREZZO          : ", row[8]
        PREZZO                    = str(row[8])
        #
        print "DATA_VALIDITA   : ", row[9]
        DATA_VALIDITA             = str(row[9])
        #
        print "DATA_VALIDITA_AL: ", row[10]
        DATA_VALIDITA_AL          = str(row[10])
        #
        print "COLONNA L       : ", row[11]
        COLONNA_L                 = str(row[11])
        #
        print "row: ", row
        #
        if (flag == 'C'):
            print "Elaborazione C-ompleta. Eseguo INSERT secca."
            cur.execute("""INSERT INTO Z_PRODOTTO_OPERANDO(
                CTAR1, 
                UTENZA, 
                ACQUISIZIONE, 
                DATA_VALIDITA,
                OPERANDO,
                VALORI,
                PRODOTTO,
                PREZZO,
                DATA_VALIDITA_AL) 
                VALUES (
                :wARG1,
                :wARG2,
                :wARG3,
                :wARG4,
                :wARG5,
                :wARG6,
                :wARG7,
                :wARG8,
                :wARG9)""", 
                wARG1 = CTAR1, 
                wARG2 = UTENZA, 
                wARG3 = ACQUISIZIONE, 
                wARG4 = DATA_VALIDITA,
                wARG5 = OPERANDO,
                wARG6 = VALORI,
                wARG7 = PRODOTTO,
                wARG8 = PREZZO,
                wARG9 = DATA_VALIDITA_AL)
            cur.execute('COMMIT') 
            ctr_I+=1
        #
        if (flag == 'P' ):
            print "Elaborazione P-arziale"
            if (COLONNA_L == 'D'):
                #verifico se la tupla esiste e allora proseguo con UPDATE altrimenti con INSERT
                print "  COLONNA_L e' pari a D e quindi cancello la tupla, se esiste nella tabella."
                print "  Eseguo SELECT di verifica esistenza prima di DELETE....."
                if (len(UTENZA) > 0):
                    cur.execute("""SELECT VALORI FROM Z_PRODOTTO_OPERANDO WHERE PRODOTTO = :wARG1 and CTAR1 = :wARG2 and UTENZA = :wARG3 and ACQUISIZIONE = :wARG4 and OPERANDO = :wARG5""",
                            wARG1 = PRODOTTO,
                            wARG2 = CTAR1,
                            wARG3 = UTENZA,
                            wARG4 = ACQUISIZIONE,
                            wARG5 = OPERANDO)
                else:
                    cur.execute("""SELECT VALORI FROM Z_PRODOTTO_OPERANDO WHERE PRODOTTO = :wARG1 and CTAR1 = :wARG2 and UTENZA is null and ACQUISIZIONE = :wARG4 and OPERANDO = :wARG5""",
                            wARG1 = PRODOTTO,
                            wARG2 = CTAR1,
                            wARG4 = ACQUISIZIONE,
                            wARG5 = OPERANDO)
                #
                res = cur.fetchone()
                if (cur.rowcount == 0):
                    print "  La SELECT e' fallita, la tupla non esiste e quindi la DELETE e' inutile."
                    print "  Ho usato:"
                    print "     PRODOTTO     = ", PRODOTTO
                    print "     CTAR1        = ", CTAR1
                    print "     UTENZA       = ", UTENZA
                    print "     ACQUISIZIONE = ", ACQUISIZIONE
                    print "     OPERANDO     = ", OPERANDO
                    
                else:
                    print "  La SELECT e' positiva, la tupla  esiste e quindi procedo con DELETE."
                    if (len(UTENZA) > 0):
                        cur.execute("""DELETE FROM Z_PRODOTTO_OPERANDO WHERE PRODOTTO = :wARG1 and CTAR1 = :wARG2 and UTENZA = :wARG3 and ACQUISIZIONE = :wARG4 and OPERANDO = :wARG5""",
                            wARG1 = PRODOTTO,
                            wARG2 = CTAR1,
                            wARG3 = UTENZA,
                            wARG4 = ACQUISIZIONE,
                            wARG5 = OPERANDO)
                    else:
                        cur.execute("""DELETE FROM Z_PRODOTTO_OPERANDO WHERE PRODOTTO = :wARG1 and CTAR1 = :wARG2 and UTENZA is null and ACQUISIZIONE = :wARG4 and OPERANDO = :wARG5""",
                            wARG1 = PRODOTTO,
                            wARG2 = CTAR1,
                            wARG4 = ACQUISIZIONE,
                            wARG5 = OPERANDO)
                    cur.execute('COMMIT') 
                    ctr_D+=1
            else:
                #verifico se la tupla esiste e allora proseguo con UPDATE altrimenti con INSERT
                "  Eseguo SELECT...."
                cur.execute("""SELECT VALORI FROM Z_PRODOTTO_OPERANDO WHERE PRODOTTO = :wARG1 and CTAR1 = :wARG2 and UTENZA = :wARG3 and ACQUISIZIONE = :wARG4 and OPERANDO = :wARG5""",
                            wARG1 = PRODOTTO,
                            wARG2 = CTAR1,
                            wARG3 = UTENZA,
                            wARG4 = ACQUISIZIONE,
                            wARG5 = OPERANDO)
                #
                res = cur.fetchone()
                if (cur.rowcount == 0):
                    print "  La SELECT non ha trovato alcuna tupla esistente e quindi eseguo INSERT..."
                    cur.execute("""INSERT INTO Z_PRODOTTO_OPERANDO(
                        CTAR1, 
                        UTENZA, 
                        ACQUISIZIONE, 
                        DATA_VALIDITA,
                        OPERANDO,
                        VALORI,
                        PRODOTTO,
                        PREZZO,
                        DATA_VALIDITA_AL) 
                        VALUES (
                        :wARG1,
                        :wARG2,
                        :wARG3,
                        :wARG4,
                        :wARG5,
                        :wARG6,
                        :wARG7,
                        :wARG8,
                        :wARG9)""", 
                        wARG1 = CTAR1, 
                        wARG2 = UTENZA, 
                        wARG3 = ACQUISIZIONE, 
                        wARG4 = DATA_VALIDITA,
                        wARG5 = OPERANDO,
                        wARG6 = VALORI,
                        wARG7 = PRODOTTO,
                        wARG8 = PREZZO,
                        wARG9 = DATA_VALIDITA_AL)
                    cur.execute('COMMIT')
                    ctr_I+=1
                else:
                    print "  La SELECT ha trovato una tupla esistente e quindi eseguo UPDATE..."
                    cur.execute("""UPDATE Z_PRODOTTO_OPERANDO SET VALORI = :wuARG0, PREZZO = :wuARG1, DATA_VALIDITA = :wuARG2, DATA_VALIDITA_AL = :wuARG3 WHERE PRODOTTO = :wqARG0 and CTAR1 = :wqARG1 and UTENZA = :wqARG2 and ACQUISIZIONE = :wqARG3 and OPERANDO = :wqARG4""",
                            wuARG0 = VALORI,
                            wuARG1 = PREZZO,
                            wuARG2 = DATA_VALIDITA,
                            wuARG3 = DATA_VALIDITA_AL,
                            wqARG0 = PRODOTTO,
                            wqARG1 = CTAR1,
                            wqARG2 = UTENZA,
                            wqARG3 = ACQUISIZIONE,
                            wqARG4 = OPERANDO)
                    cur.execute('COMMIT')
                    ctr_U+=1
                # 
#print datetime.now()
#
#db.commit()
print " "
print "ELABORAZIONE TERMINATA"
if (flag == 'C'):
    print "L'esecuzione e' avvenuta con il flag C-ompleto. Pulizia tabella e poi inserimenti."
    print "  Totale INSERT: ", ctr_I
#
if(flag == 'P'):
    print "L'esecuzione e' avvenuta con il flag P-arziale. Possibili INSERT, DELETE e UPDATE."    
    print "  Totale DELETE: ", ctr_D
    print "  Totale INSERT: ", ctr_I
    print "  Totale UPDATE: ", ctr_U

