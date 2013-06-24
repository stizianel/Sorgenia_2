!/bin/bash
#
#------------------------------------------------------------------------------------#
# A_instln_050     ------>  Aggregatore Struttura Installation                       #
#   Creanetwork S.r.l. a.rossoni 15.11.2012                                          #
#------------------------------------------------------------------------------------#
cd $PY_PROGRAMS
#
if [ -f A_instln_050.py ]
then
        if [ -x A_instln_050.py ]
	then
		python2.7 A_instln_050.py
		retStatus=$?
		exit $retStatus
        else
                exit 10 #controllare chmod....
        fi
else
	exit 11 #il programma non esiste
fi
#
