#!/bin/bash
#
#------------------------------------------------------------------------------------#
# A_adrstreet_020     ------>  Aggregatore Struttura Adrstreet Street                #
#   Creanetwork S.r.l. a.rossoni 15.11.2012                                          #
#------------------------------------------------------------------------------------#
cd $PY_PROGRAMS
#
if [ -f A_adrstreet_020.py ]
then
        if [ -x A_adrstreet_020.py ]
	then
		python2.7 A_adrstreet_020.py
		retStatus=$?
		exit $retStatus
        else
                exit 10 #controllare chmod....
        fi
else
	exit 11 #il programma non esiste
fi
#
