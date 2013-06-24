#!/bin/bash
#
#------------------------------------------------------------------------------------#
# E_billdoch_152     ------>  Estrattore  Struttura Billdoc                          #
#   Creanetwork S.r.l. a.rossoni 16.11.2012                                          #
#------------------------------------------------------------------------------------#
cd $PY_PROGRAMS
#
if [ -f E_billdoc_152.py ]
then
        if [ -x E_billdoc_152.py ]
	then
		python2.7 E_billdoc_152.py
		retStatus=$?
                #$SH_SCRIPTS/sposta.sh billdoch
		exit $retStatus
        else
                exit 10 #controllare chmod....
        fi
else
	exit 11 #il programma non esiste
fi
#
