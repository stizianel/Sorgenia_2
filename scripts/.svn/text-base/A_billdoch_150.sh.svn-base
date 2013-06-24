#!/bin/bash
#
#------------------------------------------------------------------------------------#
# A_billdoch_150     ------>  Aggregatore Struttura Billdoc                          #
#   Creanetwork S.r.l. a.rossoni 15.11.2012                                          #
#------------------------------------------------------------------------------------#
cd $PY_PROGRAMS
#
if [ -f A_billdoch_150.py ]
then
        if [ -x A_billdoch_150.py ]
	then
		python2.7 A_billdoch_150.py
		retStatus=$?
		exit $retStatus
        else
                exit 10 #controllare chmod....
        fi
else
	exit 11 #il programma non esiste
fi
#
