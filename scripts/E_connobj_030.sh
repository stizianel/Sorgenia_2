#!/bin/bash
#
#------------------------------------------------------------------------------------#
# E_connobj_030    ------>  Estrattore  Struttura Connection Object                  #
#   Creanetwork S.r.l. a.rossoni 16.11.2012                                          #
#------------------------------------------------------------------------------------#
cd $PY_PROGRAMS
#
if [ -f E_connobj_030.py ]
then
        if [ -x E_connobj_030.py ]
	then
		python2.7 E_connobj_030.py
		retStatus=$?
                $SH_SCRIPTS/sposta.sh connobj
		exit $retStatus
        else
                exit 10 #controllare chmod....
        fi
else
	exit 11 #il programma non esiste
fi
#
