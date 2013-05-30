'''
Created on 13/lug/2012

@author: stefano.tizianel
'''
import cx_Oracle
import csv
from datetime import datetime
import os
import sys

username = os.environ['username']
password = os.environ['password']
host = os.environ['host']
sid = os.environ['sid']
conninfo = username + '/' + password + '@' + host + '/' + sid
print conninfo

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
print datetime.now()
with open('./ZRES_SPSENZAPENSIERI_SP01.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        if (prima == 0):
            prima = 1
            continue
        print "CTAR1           : ", row[1]
        CTAR1                     = str(row[1])
        if (prima == 1):
            print "Pulisco la tabella per CTAR1 letto: ", CTAR1
            cur.execute("""DELETE FROM X_PRODOTTO_OPERANDO WHERE CTAR1 = :wARG1""",
            wARG1 = CTAR1)
            cur.execute('COMMIT') 
            prima = 2
        #
        print "UTENZA          : ", row[3]
        UTENZA                    = str(row[3])
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
        print "VALORI          : ", row[7]
        VALORI                    = str(row[7])
        #
        print "PRODOTTO        : ", row[0]
        PRODOTTO                  = str(row[0])
        #
        print "PREZZO          : ", row[8]
        PREZZO                    = str(row[8])
        #
        print "DATA_VALIDITA_AL: ", row[10]
        DATA_VALIDITA_AL          = str(row[10])
        #
        print "row: ", row
        #
        cur.execute("""INSERT INTO X_PRODOTTO_OPERANDO(
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
    #
        cur.execute('COMMIT') 
print datetime.now()
#
#db.commit()
print datetime.now()

