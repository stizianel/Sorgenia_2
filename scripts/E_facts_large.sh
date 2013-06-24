#!/bin/bash
#
#------------------------------------------------------------------------------------#
# E_facts_large    ------>  Estrattore  Multi Struttura Facts                        #
#   Creanetwork S.r.l. a.rossoni 17.01.2013                                          #
#------------------------------------------------------------------------------------#
cd $PY_PROGRAMS
#
if [ -f E_facts_Large.py ]
then
        if [ -x E_facts_Large.py ]
	then
		python2.7 E_factsgenLarge.py
		retStatus=$?
		exit $retStatus
        else
                exit 10 #controllare chmod....
        fi
else
	exit 11 #il programma non esiste
fi
#
