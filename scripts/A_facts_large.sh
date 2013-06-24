#!/bin/bash
#
#------------------------------------------------------------------------------------#
# A_facts_large    ------>  Aggregatore Multi Struttura Facts                        #
#   Creanetwork S.r.l. a.rossoni 17.01.2013                                          #
#------------------------------------------------------------------------------------#
cd $PY_PROGRAMS
#
if [ -f A_facts_large.py ]
then
        if [ -x A_facts_large.py ]
	then
		python2.7 A_facts_large.py
		retStatus=$?
		exit $retStatus
        else
                exit 10 #controllare chmod....
        fi
else
	exit 11 #il programma non esiste
fi
#
