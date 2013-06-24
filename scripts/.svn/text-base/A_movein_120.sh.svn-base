#!/bin/bash
#
#------------------------------------------------------------------------------------#
# A_movein_120     ------>  Aggregatore Struttura Movein                             #
#   Creanetwork S.r.l. a.rossoni 15.11.2012                                          #
#------------------------------------------------------------------------------------#
cd $PY_PROGRAMS
#
if [ -f A_movein_120.py ]
then
        if [ -x A_movein_120.py ]
	then
		python2.7 A_movein_120.py
		retStatus=$?
		exit $retStatus
        else
                exit 10 #controllare chmod....
        fi
else
	exit 11 #il programma non esiste
fi
#
