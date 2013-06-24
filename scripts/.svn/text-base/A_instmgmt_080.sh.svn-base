#!/bin/bash
#
#------------------------------------------------------------------------------------#
# A_instmgmt_080     ------>  Aggregatore Struttura Installation Management          #
#   Creanetwork S.r.l. a.rossoni 16.11.2012                                          #
#------------------------------------------------------------------------------------#
cd $PY_PROGRAMS
#
if [ -f A_instmgmt_080.py ]
then
        if [ -x A_instmgmt_080.py ]
	then
		python2.7 A_instmgmt_080.py
		retStatus=$?
		exit $retStatus
        else
                exit 10 #controllare chmod....
        fi
else
	exit 11 #il programma non esiste
fi
#
