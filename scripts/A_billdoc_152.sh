#!/bin/bash
#
#------------------------------------------------------------------------------------#
# A_billdoch_152     ------>  Aggregatore Struttura Billdoc                          #
#   ST 12.03.2013                                          #
#------------------------------------------------------------------------------------#
cd $PY_PROGRAMS
#
if [ -f A_billdoc_152.py ]
then
        if [ -x A_billdoc_152.py ]
	then
		python2.7 A_billdoc_152.py
		retStatus=$?
		exit $retStatus
        else
                exit 10 #controllare chmod....
        fi
else
	exit 11 #il programma non esiste
fi
#
