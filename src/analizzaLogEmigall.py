#!/usr/bin/env python
# -*- coding:iso-8859-1 -*-
'''
Created on 29/nov/2012

@author: andrea.rossoni - stefano tizianel
'''
import cx_Oracle
import csv
from datetime import datetime
import os
import sys
import string

username = os.environ['username']  # x stringa connessione Oracle
password = os.environ['password']  # x stringa connessione Oracle
host     = os.environ['host']      # x stringa connessione Oracle
sid      = os.environ['sid']       # x stringa connessione Oracle
#
OGGETTO  = sys.argv[1]
TIMBRO   = " "
#
conninfo = username + '/' + password + '@' + host + '/' + sid
print conninfo
print "OGGETTO Selezionato: ", OGGETTO
#
ctr_LOG    = 0
ctr_DESC   = 0  
ctr_GES    = 0
ctr_ERR    = 0
rigaXls    = 0

#
LISTAX  = []
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
#with open('./ZRES_SPSENZAPENSIERI_SP01.csv', 'rb') as f:
with open('./log2.txt', 'rb') as f:
    reader = csv.reader(f, delimiter='|')
    for row in reader:
        rigaXls+=1
        #
        if (rigaXls == 1): #prendo la data
            TIMBRO     = row[0][0:11]
            print "PRIMA RIGA"
            print "  TIMBRO: ", TIMBRO
            date       = datetime.now()
            dateformat = date.strftime("%H:%M:%S")
            TIMBRO     = TIMBRO + "- " + dateformat
            print "  TIMBRO: ", TIMBRO
            
        if (rigaXls < 6):
            
            continue    #salto le prime cinque righe di testata
        #
        print "-------------------------------------------------------------------------------------- ", str(rigaXls)
        #
        if (len(row) ==  1): # ho trovato l'aultima riga del file di log
            continue
        #print "FILLER0         : ", row[0]
        FILLER                    = row[0]
        #
        print "TIPO            : ", row[1]
        TIPO                      = row[1]
        #
        print "ERRORE          : ", row[2]
        ERRORE                    = row[2]
        #
        print "IDEN            : ", row[3]
        IDEN                      = row[3]
        #
        print "NR              : ", row[4]
        NR                        = row[4]
        #
        #print "FILLER1         : ", row[5]
        FILLER1                   = row[5]
        #
        #verifico se nella tabella ORACLE DQ_LOG_EMIGALL_DESC esiste una tupla riferita
        #alla chiave formata da IDEN+NR
        CHIAVE                    = string.strip(IDEN)+string.strip(NR)
        #
        #verifico se la tupla esiste e allora proseguo con UPDATE altrimenti con INSERT
        print "  Eseguo SELECT...."
        cur.execute("""SELECT DESCRIZIONE FROM DQ_LOG_EMIGALL_DESC WHERE CODICE = :wARG1""", wARG1 = CHIAVE)
        #
        res = cur.fetchone()
        if (cur.rowcount == 0):
            print "  La SELECT non ha trovato alcuna tupla esistente e quindi eseguo INSERT..."
            cur.execute("""INSERT INTO DQ_LOG_EMIGALL_DESC (
                        CODICE, 
                        DESCRIZIONE) 
                        VALUES (
                        :wARG1,
                        :wARG2)""", 
                        wARG1 = CHIAVE, 
                        wARG2 = ERRORE)
            cur.execute('COMMIT')
            ctr_DESC+=1
        else:
            print "La chiave ", CHIAVE, " esiste nella tabella DQ_LOG_EMIGALL_DESC."
            ctr_GES+=1
        #
        lista                     = str(row[2]).split(" ")
        if ( (lista[0] == 'Errore') and (lista[2] == 'oldkey') ):
            OLDKEY = lista[3]
            print "OLDKEY          : ", OLDKEY
            ERRORE0=ERRORE1=ERRORE2=ERRORE3=ERRORE4=ERRORE5=ERRORE6=ERRORE7=ERRORE8=ERRORE9=" "
            if(len(LISTAX) > 10):
                maxx = 10
            else:
                maxx = len(LISTAX)
            i = 0 
            #scarico il dizionario degli errori per questa oldkey
            while i < maxx: 
                print LISTAX[i] 
                ERR = "ERRORE"+str(i)
                VAL = '"'+LISTAX[i]+'"'
                exec('%s=%s') % (ERR, VAL)
                i = i + 1 
            print "ERRORE0: ", ERRORE0
            print "ERRORE1: ", ERRORE1
            print "ERRORE2: ", ERRORE2
            print "ERRORE3: ", ERRORE3
            print "ERRORE4: ", ERRORE4
            print "ERRORE5: ", ERRORE5
            print "ERRORE6: ", ERRORE6
            print "ERRORE7: ", ERRORE7
            print "ERRORE8: ", ERRORE8
            print "ERRORE9: ", ERRORE9
            #ho trovato la fine degli errori per oldkey e quindi INSERT in ORACLE
            
            cur.execute("""INSERT INTO DQ_LOG_EMIGALL(
                OGGETTO, 
                TIMBRO, 
                OLDKEY, 
                ERRORE0,
                ERRORE1,
                ERRORE2,
                ERRORE3,
                ERRORE4,
                ERRORE5,
                ERRORE6,
                ERRORE7,
                ERRORE8,
                ERRORE9
                ) 
                VALUES (
                :wARG1,
                :wARG2,
                :wARG3,
                :wARG4,
                :wARG5,
                :wARG6,
                :wARG7,
                :wARG8,
                :wARG9,
                :wARG10,
                :wARG11,
                :wARG12,
                :wARG13)""", 
                wARG1  = OGGETTO, 
                wARG2  = TIMBRO, 
                wARG3  = OLDKEY, 
                wARG4  = ERRORE0,
                wARG5  = ERRORE1,
                wARG6  = ERRORE2,
                wARG7  = ERRORE3,
                wARG8  = ERRORE4,
                wARG9  = ERRORE5,
                wARG10 = ERRORE6,
                wARG11 = ERRORE7,
                wARG12 = ERRORE8,
                wARG13 = ERRORE9)
            cur.execute('COMMIT') 
            ctr_LOG+=1
            #
            #azzero il dizionario per la prossima oldkey che andrò a trattare
            LISTAX=[]
        #
        LISTAX.append(CHIAVE)   
        ctr_ERR+=1
        # 
#print datetime.now()
#
#db.commit()
print " "
print "ELABORAZIONE TERMINATA"
print " "
print "  CONTATORI"
print "    Righe lette da file LOG                            : ", rigaXls
print "    ERRORI riscontrati                                 : ", ctr_ERR
print "    INSERT su tabella DQ_LOG_EMIGALL (OLDKEY trattate) : ", ctr_LOG
print "    Codici errore inseriti (INSERT DQ_LOG_EMIGALL_DESC): ", ctr_DESC
print "    Codici errore gia' esistenti                       : ", ctr_GES