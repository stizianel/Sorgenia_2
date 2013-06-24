#!/bin/bash
#
#------------------------------------------------------------------------------------#
# E_factsgenlarge    ------>  Estrattore  Multi Struttura Facts UNICO EMIGALL        #
#   Creanetwork S.r.l. a.rossoni 18.01.2013                                          #
#------------------------------------------------------------------------------------#
cd $PY_PROGRAMS
#
if [ -f E_factsgenLarge.py ]
then
        if [ -x E_factsgenLarge.py ]
	then
		python2.7 E_factsgenLarge.py
		retStatus=$?
                $SH_SCRIPTS/sposta.sh factsgenLarge
		exit $retStatus
        else
                exit 10 #controllare chmod....
        fi
else
	exit 11 #il programma non esiste
fi
#
