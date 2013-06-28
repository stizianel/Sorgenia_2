'''
Created on 26/giu/2013

@author: Hal
'''
import os
import subprocess
import fnmatch

path = "c://temp/sorgenia/csv/"
dirs = os.listdir( path )


print dirs

iname = raw_input ("What file do you want to convert ? ")

for name in dirs:
    if fnmatch.fnmatch(name, iname):
        print name
        a = name.split('_')       
        print a[0]
        ret = subprocess.call('dos2unix -n name a[0]')
        print ret
        

