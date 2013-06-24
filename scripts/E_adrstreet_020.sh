#!/bin/bash
#
#------------------------------------------------------------------------------------#
# E_adrstreet_020     ------>  Estrattore  Struttura Adrstreet Street                #
#   Creanetwork S.r.l. a.rossoni 15.11.2012                                          #
#------------------------------------------------------------------------------------#
cd $PY_PROGRAMS
#
if [ -f E_adrstreet_020.py ]
then
        if [ -x E_adrstreet_020.py ]
	then
		python2.7 E_adrstreet_020.py
		retStatus=$?
                $SH_SCRIPTS/sposta.sh adrstreet
		exit $retStatus
        else
                exit 10 #controllare chmod....
        fi
else
	exit 11 #il programma non esiste
fi
#
