#!/bin/bash
#
#------------------------------------------------------------------------------------#
# A_payment_140     ------>  Aggregatore Struttura Payment                           #
#   Creanetwork S.r.l. a.rossoni 16.11.2012                                          #
#------------------------------------------------------------------------------------#
cd $PY_PROGRAMS
#
if [ -f A_payment_140.py ]
then
        if [ -x A_payment_140.py ]
	then
		python2.7 A_payment_140.py
		retStatus=$?
		exit $retStatus
        else
                exit 10 #controllare chmod....
        fi
else
	exit 11 #il programma non esiste
fi
#
