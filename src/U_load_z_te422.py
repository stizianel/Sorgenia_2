'''
Created on 13/lug/2012
programma per il caricamento da file della tabella SAP ZMDA_INSTLN_INFO scaricata con SE16 nel
metodo non convertire - il file va trattato togliendo le righe di testata e l'ultima

@author: stefano.tizianel
'''
import cx_Oracle
import csv
from datetime import datetime
import os
import sys
#port itertools

username = os.environ['username']
password = os.environ['password']
host = os.environ['host']
sid = os.environ['sid']
fileinput = os.environ['fileinput']
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

listone = []
print datetime.now()
cur.execute("truncate table y_zmda_instln")
cur.execute("alter session set NLS_NUMERIC_CHARACTERS=',.'")
with open(fileinput, 'rb') as f:
    reader = csv.reader(f, delimiter='|')
    for row in reader:
        if row.__len__() <> 15:
            continue
        else:
            if row[2] == '100  ':
                row = [x.strip(' ') for x in row]
                w_resid = row[7]
                row[7] = w_resid[0:1]
                w_potda = row[10]
                w_pota  = row[11]
                print str(w_potda) + ' ' + str(w_pota)
                row[10] = w_potda
                row[11] = w_pota
                listone.append(row)
print datetime.now()
#               print listone
cur.prepare("INSERT INTO y_zmda_instln(FLAG0, FLAG1, MANDT, OPERAND, OPZ_DISTR, TIPO_USO, LIV_TENS, RESIDENZA, PROVINCIA, CD_ISTAT, POTENZA_DA, POTENZA_A, TARIFART, KONDIGR, FLAG2) VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, to_number(:11,'999G999G999D9999999'), to_number(:12,'999G999G999D9999999'), :13, :14, :15)")
cur.executemany(None, listone)
db.commit()
print datetime.now()

