#!/bin/bash
#
#------------------------------------------------------------------------------------#
# A_moveinH_120.py    ------>  Aggregatore Storico Contratti                            #
#   Creanetwork S.r.l. a.rossoni 16.11.2012                                          #
#------------------------------------------------------------------------------------#
cd $PY_PROGRAMS
#
if [ -f A_moveinH_120.py ]
then
        if [ -x A_moveinH_120.py ]
	then
		python2.7 A_moveinH_120.py
		retStatus=$?
		exit $retStatus
        else
                exit 10 #controllare chmod....
        fi
else
	exit 11 #il programma non esiste
fi
#
