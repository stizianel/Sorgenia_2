'''
Created on 05/ott/2012

@author: Creanetwork Sr.l.  Andrea Rossoni
''' 
import os
import sys
import pysap
import cx_Oracle
#
def Elabora_Partner():
    print "Entro in Elabora_Partner"
    cursor1.execute("SELECT ACDAN FROM Z_TEST_CONTRATTI WHERE SISTEMA = " + '\'' + str(sys.argv[1]) + '\'')
    ciclo = cursor1.fetchall()
    TOT   = cursor1.rowcount
    print " La SELECT ha restituito un cursore da ", str(TOT), " tuple."
    for i in ciclo:
        ACDAN = i[0]
        print " "
        print "PARTNER <--------------------------------------------------------------"
        print "  Sto elaborando il ACDAN: ", str(ACDAN)
        print "  Ora vado ad eseguire la Query su SAP....."
        #
        campo_temksv = ['newkey']
        #
        direttive    = "object = 'PARTNER' AND oldkey = " + '\'' + str(ACDAN) + '\''
        print "  direttive: ", direttive
        TUPLA        = sap_conn.read_table('TEMKSV',options=[direttive],fields=campo_temksv,max_rows=1)
        #
        if(TUPLA.count == 0):
            valore     = "N.A."
            print "  Tupla non trovata in SAP, imposto default."
        else: 
            row_temksv = TUPLA.get_line(0)
            valore     = row_temksv.newkey.ext_value
            print "  Valore letto da SAP      : ", valore
            valore = int(valore)
            print "  Valore che uso per UPDATE: ", str(valore)
        #
        print "  Eseguo UPDATE su Z_TEST_CONTRATTI..."
        aggiornaTab = "UPDATE Z_TEST_CONTRATTI SET PARTNER = " + '\'' + str(valore) + '\'' + " WHERE ACDAN = " + '\''+ str(ACDAN) + '\'' + " AND SISTEMA = " + '\'' + sys.argv[1] + '\''
        print "  Eseguo: ", aggiornaTab
        cursor2.execute("UPDATE Z_TEST_CONTRATTI SET PARTNER = :arg1  WHERE ACDAN = :arg2 AND SISTEMA = :arg3", arg1 = str(valore), arg2 = str(ACDAN), arg3 = sys.argv[1])
        cursor2.execute("commit")
#
def Elabora_Movein():
    print "Entro in Elabora_Movein"
    cursor1.execute("SELECT CNCON FROM Z_TEST_CONTRATTI WHERE SISTEMA = " + '\'' + str(sys.argv[1]) + '\'')
    ciclo = cursor1.fetchall()
    TOT   = cursor1.rowcount
    print " La SELECT ha restituito un cursore da ", str(TOT), " tuple."
    for i in ciclo:
        CNCON = i[0]
        print " "
        print "MOVEIN <--------------------------------------------------------------"
        print "  Sto elaborando il CNCON: ", str(CNCON)
        print "  Ora vado ad eseguire la Query su SAP....."
        #
        campo_temksv = ['newkey']
        #
        direttive    = "object = 'MOVE_IN' AND oldkey = " + '\'' + str(CNCON) + '\''
        print "  direttive: ", direttive
        TUPLA        = sap_conn.read_table('TEMKSV',options=[direttive],fields=campo_temksv,max_rows=1)
        #
        if(TUPLA.count == 0):
            valore     = "N.A."
            print "  Tupla non trovata in SAP, imposto default."
        else: 
            row_temksv = TUPLA.get_line(0)
            valore     = row_temksv.newkey.ext_value
            print "  Valore letto da SAP      : ", valore
            valore = int(valore)
            print "  Valore che uso per UPDATE: ", str(valore)
        #
        print "  Eseguo UPDATE su Z_TEST_CONTRATTI..."
        aggiornaTab = "UPDATE Z_TEST_CONTRATTI SET MOVEIN = " + '\'' + str(valore) + '\'' + " WHERE CNCON = " + '\''+ str(CNCON) + '\'' + " AND SISTEMA = " + '\'' + sys.argv[1] + '\''
        print "  Eseguo: ", aggiornaTab
        cursor2.execute("UPDATE Z_TEST_CONTRATTI SET MOVEIN = :arg1  WHERE CNCON = :arg2 AND SISTEMA = :arg3", arg1 = str(valore), arg2 = str(CNCON), arg3 = sys.argv[1])
        cursor2.execute("commit")
#
def Elabora_Instln():
    print "Entro in Elabora_Instln"
    cursor1.execute("SELECT CNCON FROM Z_TEST_CONTRATTI WHERE SISTEMA = " + '\'' + str(sys.argv[1]) + '\'')
    ciclo = cursor1.fetchall()
    TOT   = cursor1.rowcount
    print " La SELECT ha restituito un cursore da ", str(TOT), " tuple."
    for i in ciclo:
        CNCON = i[0]
        print " "
        print "INSTLN <--------------------------------------------------------------"
        print "  Sto elaborando il CNCON: ", str(CNCON)
        print "  Ora vado ad eseguire la Query su SAP....."
        #
        campo_temksv = ['newkey']
        #
        direttive    = "object = 'INSTLN' AND oldkey = " + '\'' + str(CNCON) + '\''
        print "  direttive: ", direttive
        TUPLA        = sap_conn.read_table('TEMKSV',options=[direttive],fields=campo_temksv,max_rows=1)
        #
        if(TUPLA.count == 0):
            valore     = "N.A."
            print "  Tupla non trovata in SAP, imposto default."
        else: 
            row_temksv = TUPLA.get_line(0)
            valore     = row_temksv.newkey.ext_value
            print "  Valore letto da SAP      : ", valore
            valore = int(valore)
            print "  Valore che uso per UPDATE: ", str(valore)
        #
        print "  Eseguo UPDATE su Z_TEST_CONTRATTI..."
        aggiornaTab = "UPDATE Z_TEST_CONTRATTI SET INSTLN= " + '\'' + str(valore) + '\'' + " WHERE CNCON = " + '\''+ str(CNCON) + '\'' + " AND SISTEMA = " + '\'' + sys.argv[1] + '\''
        print "  Eseguo: ", aggiornaTab
        cursor2.execute("UPDATE Z_TEST_CONTRATTI SET INSTLN = :arg1  WHERE CNCON = :arg2 AND SISTEMA = :arg3", arg1 = str(valore), arg2 = str(CNCON), arg3 = sys.argv[1])
        cursor2.execute("commit")
#
def Elabora_Account():
    print "Entro in Elabora_Account"
    cursor1.execute("SELECT CFLG9 FROM Z_TEST_CONTRATTI WHERE SISTEMA = " + '\'' + str(sys.argv[1]) + '\'')
    ciclo = cursor1.fetchall()
    TOT   = cursor1.rowcount
    print " La SELECT ha restituito un cursore da ", str(TOT), " tuple."
    for i in ciclo:
        CFLG9 = i[0]
        print " "
        print "ACCOUNT <--------------------------------------------------------------"
        print "  Sto elaborando il CFLG9: ", str(CFLG9)
        print "  Ora vado ad eseguire la Query su SAP....."
        #
        campo_temksv = ['newkey']
        #
        direttive    = "object = 'ACCOUNT' AND oldkey = " + '\'' + str(CFLG9) + '\''
        print "  direttive: ", direttive
        TUPLA        = sap_conn.read_table('TEMKSV',options=[direttive],fields=campo_temksv,max_rows=1)
        #
        if(TUPLA.count == 0):
            valore     = "N.A."
            print "  Tupla non trovata in SAP, imposto default."
        else: 
            row_temksv = TUPLA.get_line(0)
            valore     = row_temksv.newkey.ext_value
            print "  Valore letto da SAP      : ", valore
            valore = int(valore)
            print "  Valore che uso per UPDATE: ", str(valore)
        #
        print "  Eseguo UPDATE su Z_TEST_CONTRATTI..."
        aggiornaTab = "UPDATE Z_TEST_CONTRATTI SET ACCOUNT = " + '\'' + str(valore) + '\'' + " WHERE CFLG9 = " + '\''+ str(CFLG9) + '\'' + " AND SISTEMA = " + '\'' + sys.argv[1] + '\''
        print "  Eseguo: ", aggiornaTab
        cursor2.execute("UPDATE Z_TEST_CONTRATTI SET ACCOUNT = :arg1  WHERE CFLG9 = :arg2 AND SISTEMA = :arg3", arg1 = str(valore), arg2 = str(CFLG9), arg3 = sys.argv[1])
        cursor2.execute("commit")
#
def Elabora_Devinforec():
    print "Entro in Elabora_Devinforec"
    cursor1.execute("SELECT CNCON, MATRICOLA FROM Z_TEST_CONTRATTI WHERE SISTEMA = " + '\'' + str(sys.argv[1]) + '\'')
    ciclo = cursor1.fetchall()
    TOT   = cursor1.rowcount
    print " La SELECT ha restituito un cursore da ", str(TOT), " tuple."
    for i in ciclo:
        CNCON  = i[0]
        MATRI  = i[1]
        CHIAVE = str(MATRI)+str(CNCON)
        print " "
        print "DEVINFOREC <--------------------------------------------------------------"
        print "  Sto elaborando il CNCON: ", str(CNCON)
        print "  Ora vado ad eseguire la Query su SAP....."
        #
        campo_temksv = ['newkey']
        #
        direttive    = "object = 'DEVINFOREC' AND oldkey = " + '\'' + str(CHIAVE) + '\''
        print "  direttive: ", direttive
        TUPLA        = sap_conn.read_table('TEMKSV',options=[direttive],fields=campo_temksv,max_rows=1)
        #
        if(TUPLA.count == 0):
            valore     = "N.A."
            print "  Tupla non trovata in SAP, imposto default."
        else: 
            row_temksv = TUPLA.get_line(0)
            valore     = row_temksv.newkey.ext_value
            print "  Valore letto da SAP      : ", valore
            valore = int(valore)
            print "  Valore che uso per UPDATE: ", str(valore)
        #
        print "  Eseguo UPDATE su Z_TEST_CONTRATTI..."
        aggiornaTab = "UPDATE Z_TEST_CONTRATTI SET DEVINFOREC = " + '\'' + str(valore) + '\'' + " WHERE CNCON = " + '\''+ str(CNCON) + '\'' + " AND SISTEMA = " + '\'' + sys.argv[1] + '\''
        print "  Eseguo: ", aggiornaTab
        cursor2.execute("UPDATE Z_TEST_CONTRATTI SET DEVINFOREC = :arg1  WHERE CNCON = :arg2 AND SISTEMA = :arg3", arg1 = str(valore), arg2 = str(CNCON), arg3 = sys.argv[1])
        cursor2.execute("commit")
#
#
ora_db1_Username    = os.environ['ora_db1_username']
ora_db1_Password    = os.environ['ora_db1_password']
ora_db1_Host        = os.environ['ora_db1_host']
ora_db1_Port        = os.environ['ora_db1_port']
ora_db1_Sid         = os.environ['ora_db1_sid']

conninfo_db1        = ora_db1_Username + '/' + ora_db1_Password + '@' +ora_db1_Host + ':' + ora_db1_Port + '/' + ora_db1_Sid
#
print "Conninfo SAP: sapconn.ini con entry: ", sys.argv[1]
print "  tento la connessione a SAP......"
#
sap_conn=pysap.Rfc_connection(conn_file='sapconn.ini',conn_name=sys.argv[1])
sap_conn.open()
#
print "Conninfo DB1: ", conninfo_db1
print "  tento la connessione a Oracle..."
try:
    db1     = cx_Oracle.connect(conninfo_db1)
    cursor1 = db1.cursor()
    cursor2 = db1.cursor()
#    cur3   = db.cursor()
except cx_Oracle.DatabaseError, exc:
    error, = exc.args
    print "Oracle-Error-Code:", error.code
    print "Oracle-Error-Message:", error.message
    print "La connessione al DB ORACLE fallita !"
    sys.exit()
#
print "La connessione al DB Oracle e' avvenuta correttamente."
#
cursor1.execute("ALTER SESSION SET NLS_DATE_FORMAT = 'YYYYMMDD HH24:MI:SS'")
#
#
if len(sys.argv) == 1:
    print "Non ci sono parametri in ingresso. Esco !"
    sys.exit()
print "Len di argv: ", len(sys.argv)
# le connessioni ai DB SAP e Oracle sono OK e anche i parametri in linea, quindi procedo!
#print "-------------------------------------------------------------------------------------------------------"
for ctr in range (2, len(sys.argv)):
    #
    if   sys.argv[ctr] == 'PARTNER':
        print "Eseguo la sezione dedicata a: ", sys.argv[ctr]
        Elabora_Partner()
    elif sys.argv[ctr] == 'ACCOUNT':
        print "Eseguo la sezione dedicata a: ", sys.argv[ctr]
        Elabora_Account()
    elif sys.argv[ctr] == 'DEVINFOREC':
        print "Eseguo la sezione dedicata a: ", sys.argv[ctr]
        Elabora_Devinforec()
    elif sys.argv[ctr] == 'MOVEIN':
        print "Eseguo la sezione dedicata a: ", sys.argv[ctr]
        Elabora_Movein()
    elif sys.argv[ctr] == 'INSTLN':
        print "Eseguo la sezione dedicata a: ", sys.argv[ctr]
        Elabora_Instln()
    else:
        print "La struttura ", sys.argv[ctr], " non e' codificata e quindi non puo' essere elaborata. Skippo..." 
#----------------------------------------------------------------------------------------------------------------
print "#---------------------------------------------------------------------------------------------------------#"
print "#--------------------------------->F   I   N   I   T   O<-------------------------------------------------#"
print "#---------------------------------------------------------------------------------------------------------#"
del db1
cursor1.close()
cursor2.close()