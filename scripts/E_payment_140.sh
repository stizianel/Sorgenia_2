#!/bin/bash
#
#------------------------------------------------------------------------------------#
# E_payment_140     ------>  Estrattore  Struttura Payment                           #
#   Creanetwork S.r.l. a.rossoni 16.11.2012                                          #
#------------------------------------------------------------------------------------#
cd $PY_PROGRAMS
#
if [ -f E_payment_140.py ]
then
        if [ -x E_payment_140.py ]
	then
		python2.7 E_payment_140.py
		retStatus=$?
                $SH_SCRIPTS/sposta.sh payment
		exit $retStatus
        else
                exit 10 #controllare chmod....
        fi
else
	exit 11 #il programma non esiste
fi
#
