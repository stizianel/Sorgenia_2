#!/bin/bash
#
#------------------------------------------------------------------------------------#
# E_facts_Gas ------>  Aggregatore Struttura Facts Gas                                  #
#   Creanetwork S.r.l. a.rossoni 20.11.2012                                          #
#------------------------------------------------------------------------------------#
cd $PY_PROGRAMS
#
if [ -f A_facts_Gas.py ]
then
        if [ -x A_facts_Gas.py ]
	then
		python2.7 A_facts_Gas.py
		retStatus=$?
		exit $retStatus
        else
                exit 10 #controllare chmod....
        fi
else
	exit 11 #il programma non esiste
fi
#
