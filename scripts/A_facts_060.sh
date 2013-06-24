#!/bin/bash
#
#------------------------------------------------------------------------------------#
# E_facts_060 ------>  Aggregatore Struttura Facts                                   #
#   Creanetwork S.r.l. a.rossoni 15.11.2012                                          #
#------------------------------------------------------------------------------------#
cd $PY_PROGRAMS
#
if [ -f A_facts_060.py ]
then
        if [ -x A_facts_060.py ]
	then
		python2.7 A_facts_060.py
		retStatus=$?
		exit $retStatus
        else
                exit 10 #controllare chmod....
        fi
else
	exit 11 #il programma non esiste
fi
#
