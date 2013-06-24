#!/bin/bash
#
#------------------------------------------------------------------------------------#
# E_instmgmt_080     ------>  Estrattore  Struttura Installation Management          #
#   Creanetwork S.r.l. a.rossoni 16.11.2012                                          #
#------------------------------------------------------------------------------------#
cd $PY_PROGRAMS
#
if [ -f E_instmgmt_080.py ]
then
        if [ -x E_instmgmt_080.py ]
	then
		python2.7 E_instmgmt_080.py
		retStatus=$?
#                $SH_SCRIPTS/sposta.sh instmgmt
		exit $retStatus
        else
                exit 10 #controllare chmod....
        fi
else
	exit 11 #il programma non esiste
fi
#
