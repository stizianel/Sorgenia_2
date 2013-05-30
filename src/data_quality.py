'''
Created on 22/nov/2012

@author: andrea.rossoni
'''
from it_eutile_utils_properties.Constants         import Constants
from it_eutile_utils_csvmanager.CsvManager        import CsvManager
from it_eutile_utils_properties.ReadConfigManager import ReadConfigManager
import cx_Oracle
import csv
from datetime import datetime
import os
import sys
import xlwt
#
from xml.dom.minidom import parse, parseString
#
parser   = parse('dq.xml')
dati     = dict()
#
username = os.environ['username']  # x stringa connessione Oracle
password = os.environ['password']  # x stringa connessione Oracle
host     = os.environ['host']      # x stringa connessione Oracle
sid      = os.environ['sid']       # x stringa connessione Oracle
#
print   os.environ['EmigallExtension']   
                                   # P-arziale 
                                   #   esegue UPDATE se trovata chiave in Tabella Z_PRODOTTO_OPERANDO
                                   #   esegue DELETE se colonna "L"  pari a "D" su Tabella Z_PRODOTTO_OPERANDO
                                   #   esegue INSERT se chiave mancante in Tabella Z_PRODOTTO_OPERANDO
conninfo = username + '/' + password + '@' + host + '/' + sid
print conninfo
#
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
styleBlack      = xlwt.easyxf('font: name Calibri size 12, color-index black,  bold off; pattern: pattern solid, fore_colour light_green, back_colour light_green', num_format_str='#,##0')
styleRosso      = xlwt.easyxf('font: name Calibri size 12, color-index red,    bold on;  pattern: pattern solid, fore_colour light_green, back_colour light_green', num_format_str='#,##0.00')
styleGiallo     = xlwt.easyxf('font: name Calibri size 12, color-index orange, bold on;  pattern: pattern solid, fore_colour light_green, back_colour light_green', num_format_str='#,##0.00')
styleBluX       = xlwt.easyxf('font: name Calibri size 14, color-index blue,   bold on;  pattern: pattern solid, fore_colour light_green, back_colour light_green', num_format_str='#,##0.00' "borders: top double, bottom double, left double, right double;")
styleBlu        = xlwt.easyxf('font: name Calibri size 14, color-index blue,   bold on;  pattern: pattern solid, fore_colour light_green, back_colour light_green', num_format_str='#,##0.00')
styleBluR       = xlwt.easyxf('font: name Calibri size 14, color-index blue,   bold on;  pattern: pattern solid, fore_colour light_green, back_colour light_green; align: wrap on, horiz right', num_format_str='#,##0.00')
style1          = xlwt.easyxf(num_format_str='D-MMM-YY')
styleLink       = xlwt.easyxf('font: name Calibri size 12, color-index blue,   bold off, underline single;pattern: pattern solid, fore_colour light_green, back_colour light_green; align: wrap on, horiz right')
styleFiller     = xlwt.easyxf('pattern: pattern solid, fore_colour dark_green, back_colour dark_green')
#
date            = datetime.now()
dateformat      = date.strftime("%Y%m%d-%H%M%S")
dateformat1     = date.strftime("%d/%m/%Y")
#
#
wb = xlwt.Workbook()
ws = wb.add_sheet("Data Quality")
#
ws.write(0, 0, "Milano,  "+dateformat1, styleBlack)
ws.write(0, 1, "("+dateformat+")",      styleBlack)
ws.write(0, 2, " ",                     styleBlack)
ws.write(0, 3, " ",                     styleBlack)
#
ws.write(1, 0, " ",                     styleFiller)
ws.write(1, 1, " ",                     styleFiller)
ws.write(1, 2, " ",                     styleFiller)
ws.write(1, 3, " ",                     styleFiller)
#
ws.write(2, 0, "ID",                    styleBlu)
ws.write(2, 1, "DESCRIZIONE",           styleBlu)
ws.write(2, 2, "TUPLE",                 styleBluR)
ws.write(2, 3, "RISULTATI QUERY",       styleBluR)
#
ws.write(3, 0, " ",                     styleFiller)
ws.write(3, 1, " ",                     styleFiller)
ws.write(3, 2, " ",                     styleFiller)
ws.write(3, 3, " ",                     styleFiller)
#
rcm          = ReadConfigManager('CSVOutput')
path         = rcm.getProperty('EmigallOutputPath')
extension    = rcm.getProperty('extension')
print "extension: ", extension
cartella     = path+"dettagli_dataQuality_"+dateformat
os.makedirs(cartella)
#
prima        = 0
riga         = 4
yy           = 1
linesToWrite = []
#cur.execute("ALTER SESSION SET NLS_DATE_FORMAT = 'YYYYMMDD HH24:MI:SS'")
#print datetime.now()
for queries in parser.getElementsByTagName("root"):
    for query in queries.getElementsByTagName("query"):
        
        
        for contenuto in query.getElementsByTagName("id"):
            for xo in contenuto.childNodes:
                wID = xo.data
        for contenuto in query.getElementsByTagName("descrizione"):
            for xo in contenuto.childNodes:
                wDESCRIZIONE = xo.data
        for contenuto in query.getElementsByTagName("select"):
            for xo in contenuto.childNodes:
                wSELECT = xo.data
        #dati[wID] = { "Descrizione": wDESCRIZIONE, "SELECT": wSELECT }
        print "-------------------------------------------------------------------------------------"
        print "ID: ", wID
        print "            DESCRIZIONE: ", wDESCRIZIONE
        print "            SELECT     : ", wSELECT
        #
        cur.execute(wSELECT)
        res = cur.fetchall()
        print "Il cursore ha restituito ", str(cur.rowcount), " tuple."
        if (wID[0] == 'A'):
            ws.write(int(riga), 0, wID, styleRosso)
        if (wID[0] == 'W'):
            ws.write(int(riga), 0, wID, styleGiallo)   
        ws.write(int(riga), 1, wDESCRIZIONE, styleBlack)
        ws.write(int(riga), 2, cur.rowcount, styleBlack)
        #
        if (cur.rowcount <> 0):
            #inizializzazione e apertura file emigall
            mycsv  = CsvManager("dettagli_dataQuality_"+dateformat+'\\'+wID,'\t',False)
            pippo  = mycsv.csvFileName.replace('$s',str(yy))
            link   = 'HYPERLINK("'+pippo+'";"cliccami....")'
            #print "LINK : ", link
            ws.write(int(riga), 3, xlwt.Formula(link), styleLink)
            riga+=1
            #print "mycsv: ", mycsv
            with open(mycsv.csvFileName.replace('$s',str(yy)), 'wb') as f:
                csv.register_dialect('emigall', delimiter=';',quotechar="", quoting=csv.QUOTE_NONE)
                dialect = csv.get_dialect('emigall')
                writer = csv.writer(f,dialect)
                
                for record_s1 in res:
                    #
                    linesToWrite.append(record_s1)
                    writer.writerows(linesToWrite)
                    linesToWrite=[]
        #
        else:
            ws.write(int(riga), 3, " ", styleBlack)
            riga+=1
ws.col(0).width = 3333 * 2 # 3333 = 1" (one inch).
ws.col(1).width = 3333 * 4
ws.col(2).width = 3333
ws.col(3).width = 3333 * 2
#ws.insert_bitmap('logo_creanetwork_piccola.bmp', int(riga+1), 0)
#
wb.save(path+'dataQuality_'+dateformat+'.xls')
print "*  E L A B O R A Z I O N E       C O N C L U S A  *"
#
for filename in os.listdir(cartella):
    print  filename

