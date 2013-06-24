#!/bin/bash
#
#------------------------------------------------------------------------------------#
# A_devinforec_070     ------>  Aggregatore Struttura Device Info Record             #
#   Creanetwork S.r.l. a.rossoni 16.11.2012                                          #
#------------------------------------------------------------------------------------#
cd $PY_PROGRAMS
#
if [ -f A_devinforec_070.py ]
then
        if [ -x A_devinforec_070.py ]
	then
		python2.7 A_devinforec_070.py
		retStatus=$?
		exit $retStatus
        else
                exit 10 #controllare chmod....
        fi
else
	exit 11 #il programma non esiste
fi
#
