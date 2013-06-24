#!/bin/bash
#
#------------------------------------------------------------------------------------#
# A_document_130     ------>  Aggregatore Struttura Document                         #
#   Creanetwork S.r.l. a.rossoni 16.11.2012                                          #
#------------------------------------------------------------------------------------#
cd $PY_PROGRAMS
#
if [ -f A_document_130.py ]
then
        if [ -x A_document_130.py ]
	then
		python2.7 A_document_130.py
		retStatus=$?
		exit $retStatus
        else
                exit 10 #controllare chmod....
        fi
else
	exit 11 #il programma non esiste
fi
#
