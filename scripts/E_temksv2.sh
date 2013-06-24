#!/bin/bash
#
#------------------------------------------------------------------------------------#
# E_premise_040    ------>  Estrattore  Struttura Premise                            #
#   Creanetwork S.r.l. a.rossoni 15.11.2012                                          #
#------------------------------------------------------------------------------------#
cd $PY_PROGRAMS
#
if [ -f E_Temksv2.py ]
then
        if [ -x E_premise_040.py ]
	then
		python2.7 E_Temksv2.py
		retStatus=$?
		exit $retStatus
        else
                exit 10 #controllare chmod....
        fi
else
	exit 11 #il programma non esiste
fi
#
