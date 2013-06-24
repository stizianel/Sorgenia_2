#!/bin/bash
#
#------------------------------------------------------------------------------------#
# E_devinforec_070     ------>  Estrattore  Struttura Device Info Record             #
#   Creanetwork S.r.l. a.rossoni 16.11.2012                                          #
#------------------------------------------------------------------------------------#
cd $PY_PROGRAMS
#
if [ -f E_devinforec_070.py ]
then
        if [ -x E_devinforec_070.py ]
	then
		python2.7 E_devinforec_070.py
		retStatus=$?
#                $SH_SCRIPTS/sposta.sh devinforec
		exit $retStatus
        else
                exit 10 #controllare chmod....
        fi
else
	exit 11 #il programma non esiste
fi
#
