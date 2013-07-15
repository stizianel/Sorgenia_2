'''
Created on 13/lug/2013

@author: Hal
'''
import csv

reader = csv.reader(open("c://temp//sorgenia//csv//billdoc_20130626-191404_N1.txt"), delimiter='\t')
for row in reader:
    if row[1] == 'ERCH':
        dep_lk = row[0]
        print 'tipo ' + row[1] + ' dep ' + dep_lk