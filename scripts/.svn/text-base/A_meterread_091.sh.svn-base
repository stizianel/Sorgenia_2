#!/bin/bash
#
#------------------------------------------------------------------------------------#
# A_meterread_091     ------>  Aggregatore Struttura Meterread (letture successive a #
#                              lettura tappo.)                                       #
#   Creanetwork S.r.l. a.rossoni 16.11.2012                                          #
#------------------------------------------------------------------------------------#
cd $PY_PROGRAMS
#
if [ -f A_meterread_091.py ]
then
        if [ -x A_meterread_091.py ]
	then
		python2.7 A_meterread_091.py
		retStatus=$?
		exit $retStatus
        else
                exit 10 #controllare chmod....
        fi
else
	exit 11 #il programma non esiste
fi
#
