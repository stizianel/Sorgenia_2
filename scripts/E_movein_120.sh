#!/bin/bash
#
#------------------------------------------------------------------------------------#
# E_movein_120     ------>  Estrattore  Struttura Movein                             #
#   Creanetwork S.r.l. a.rossoni 15.11.2012                                          #
#------------------------------------------------------------------------------------#
cd $PY_PROGRAMS
#
if [ -f E_movein_120.py ]
then
        if [ -x E_movein_120.py ]
	then
		python2.7 E_movein_120.py
		retStatus=$?
#                $SH_SCRIPTS/sposta.sh movein
		exit $retStatus
        else
                exit 10 #controllare chmod....
        fi
else
	exit 11 #il programma non esiste
fi
#
