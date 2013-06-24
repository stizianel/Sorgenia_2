!/bin/bash
#
#------------------------------------------------------------------------------------#
# E_account_110    ------>  Estrattore  Struttura Account                            #
#   Creanetwork S.r.l. a.rossoni 15.11.2012                                          #
#------------------------------------------------------------------------------------#
cd $PY_PROGRAMS
#
if [ -f E_account_110.py ]
then
        if [ -x E_account_110.py ]
	then
		python2.7 E_account_110.py
		retStatus=$?
#                $SH_SCRIPTS/sposta.sh account
		exit $retStatus
        else
                exit 10 #controllare chmod....
        fi
else
	exit 11 #il programma non esiste
fi
#
