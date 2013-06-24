#!/bin/bash
#
#------------------------------------------------------------------------------------#
# E_factsgen ------->  Estrattore Struttura Facts                                    #
#   Creanetwork S.r.l.  a.rossoni  15.12.2012                                        #
#------------------------------------------------------------------------------------#
cd $PY_PROGRAMS
#
if [ -f E_factsgen.py ]
then
        if [ -x E_factsgen.py ]
	then
		python2.7 E_factsgen.py
		retStatus=$?
                $SH_SCRIPTS/sposta.sh factsgen
		exit $retStatus
        else
                exit 10 #controllare chmod....
        fi
else
	exit 11 #il programma non esiste
fi
#
