#!/bin/bash
#
#------------------------------------------------------------------------------------#
# E_meterread_090     ------>  Estrattore  Struttura Meterread (lettura tappo)       #
#   Creanetwork S.r.l. a.rossoni 16.11.2012                                          #
#------------------------------------------------------------------------------------#
cd $PY_PROGRAMS
#
if [ -f E_meterread_090.py ]
then
        if [ -x E_meterread_090.py ]
	then
		python2.7 E_meterread_090.py
		retStatus=$?
#                $SH_SCRIPTS/sposta.sh meterread
		exit $retStatus
        else
                exit 10 #controllare chmod....
        fi
else
	exit 11 #il programma non esiste
fi
#
