#!/bin/bash
#
#------------------------------------------------------------------------------------#
# E_adrcity_010    ------>  Estrattore  Struttura AdrCity                            #
#   Creanetwork S.r.l. a.rossoni 16.11.2012                                          #
#------------------------------------------------------------------------------------#
cd $PY_PROGRAMS
#
if [ -f E_adrcity_010.py ]
then
        if [ -x E_adrcity_010.py ]
	then
		python2.7 E_adrcity_010.py
		retStatus=$?
                $SH_SCRIPTS/sposta.sh adrcity
		exit $retStatus
        else
                exit 10 #controllare chmod....
        fi
else
	exit 11 #il programma non esiste
fi
#
