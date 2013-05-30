'''
Created on 09/mag/2013

@author: stefano.tizianel
'''
import cx_Oracle

connstr = "SAP_USER" + '/' + "sap_user" + '@' + "192.168.0.177" + ':' + "1521" + '/' + "SINPROD"
conn = cx_Oracle.connect(connstr)
curs = conn.cursor()
curs.execute('select 2+2 "aaa" ,3*3 from dual')

curs.execute("select sysdate from dual")
print curs.fetchone()

curs.execute("ALTER SESSION SET NLS_DATE_FORMAT = 'YYYYMMDD'")
curs.execute("select sysdate from dual")
curs.execute("select to_char(sysdate) from dual")
print curs.fetchone()

curs.execute("ALTER SESSION SET NLS_DATE_FORMAT = 'YYYYMMDDHH24MISS'")
curs.execute("select sysdate from dual")
curs.execute("select to_char(sysdate) from dual")
print curs.fetchone()

conn.close()

