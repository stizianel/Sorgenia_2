#!/bin/bash
#
#------------------------------------------------------------------------------------#
# A_premise_040    ------>  Aggregatore Struttura Premise                            #
#   Creanetwork S.r.l. a.rossoni 15.11.2012                                          #
#------------------------------------------------------------------------------------#
cd $PY_PROGRAMS
#
if [ -f A_premise_040.py ]
then
        if [ -x A_premise_040.py ]
	then
		python2.7 A_premise_040.py
		retStatus=$?
		exit $retStatus
        else
                exit 10 #controllare chmod....
        fi
else
	exit 11 #il programma non esiste
fi
#
