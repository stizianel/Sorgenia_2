!/bin/bash
#
#------------------------------------------------------------------------------------#
# E_instln_050     ------>  Estrattore  Struttura Installation                       #
#   Creanetwork S.r.l. a.rossoni 15.11.2012                                          #
#------------------------------------------------------------------------------------#
cd $PY_PROGRAMS
#
if [ -f E_instln_050.py ]
then
        if [ -x E_instln_050.py ]
	then
		python2.7 E_instln_050.py
		retStatus=$?
                $SH_SCRIPTS/sposta.sh instln
		exit $retStatus
        else
                exit 10 #controllare chmod....
        fi
else
	exit 11 #il programma non esiste
fi
#
