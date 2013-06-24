#!/bin/bash
#

set -x 

#------------------------------------------------------------------------------------#
# E_interazioni     ------>  Estrattore  csv  interazioni                            #
#   Creanetwork S.r.l. ST        30.04.2013                                          #
#------------------------------------------------------------------------------------#
cd $PY_PROGRAMS
#
if [ -f E_interazioni.py ]
then
        if [ -x E_interazioni.py ]
	then
		python2.7 E_interazioni.py
		retStatus=$?
#                $SH_SCRIPTS/sposta.sh movein
		exit $retStatus
        else
                exit 10 #controllare chmod....
        fi
else
	exit 11 #il programma non esiste
fi
#
