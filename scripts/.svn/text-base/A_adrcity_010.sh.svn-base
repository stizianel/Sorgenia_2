#!/bin/bash
#
#------------------------------------------------------------------------------------#
# A_adrcity_010    ------>  Aggregatore Struttura AdrCity                            #
#   Creanetwork S.r.l. a.rossoni 16.11.2012                                          #
#------------------------------------------------------------------------------------#
cd $PY_PROGRAMS
#
if [ -f A_adrcity_010.py ]
then
        if [ -x A_adrcity_010.py ]
	then
		python2.7 A_adrcity_010.py
		retStatus=$?
		exit $retStatus
        else
                exit 10 #controllare chmod....
        fi
else
	exit 11 #il programma non esiste
fi
#
