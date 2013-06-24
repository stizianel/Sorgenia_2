!/bin/bash
#
#------------------------------------------------------------------------------------#
# A_account_110    ------>  Aggregatore Struttura Account                            #
#   Creanetwork S.r.l. a.rossoni 15.11.2012                                          #
#------------------------------------------------------------------------------------#
cd $PY_PROGRAMS
#
if [ -f A_account_110.py ]
then
        if [ -x A_account_110.py ]
	then
		python2.7 A_account_110.py
		retStatus=$?
		exit $retStatus
        else
                exit 10 #controllare chmod....
        fi
else
	exit 11 #il programma non esiste
fi
#
