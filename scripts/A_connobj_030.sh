#!/bin/bash
#
#------------------------------------------------------------------------------------#
# A_connobj_030    ------>  Aggregatore Struttura Connection Object                  #
#   Creanetwork S.r.l. a.rossoni 16.11.2012                                          #
#------------------------------------------------------------------------------------#
cd $PY_PROGRAMS
#
if [ -f A_connobj_030.py ]
then
        if [ -x A_connobj_030.py ]
	then
		python2.7 A_connobj_030.py
		retStatus=$?
		exit $retStatus
        else
                exit 10 #controllare chmod....
        fi
else
	exit 11 #il programma non esiste
fi
#
