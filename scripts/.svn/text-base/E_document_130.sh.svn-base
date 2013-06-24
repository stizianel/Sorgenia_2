#!/bin/bash
#
#------------------------------------------------------------------------------------#
# E_document_130     ------>  Estrattore  Struttura Document                         #
#   Creanetwork S.r.l. a.rossoni 16.11.2012                                          #
#------------------------------------------------------------------------------------#
cd $PY_PROGRAMS
#
if [ -f E_document_130.py ]
then
        if [ -x E_document_130.py ]
	then
		python2.7 E_document_130.py
		retStatus=$?
                #$SH_SCRIPTS/sposta.sh document
		exit $retStatus
        else
                exit 10 #controllare chmod....
        fi
else
	exit 11 #il programma non esiste
fi
#
