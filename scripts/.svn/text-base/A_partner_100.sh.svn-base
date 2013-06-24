!/bin/bash
#
#------------------------------------------------------------------------------------#
# A_partner_100    ------>  Aggregatore Struttura Partner                            #
#   Creanetwork S.r.l. a.rossoni 15.11.2012                                          #
#------------------------------------------------------------------------------------#
cd $PY_PROGRAMS
#
if [ -f A_partner_100.py ]
then
        if [ -x A_partner_100.py ]
	then
		python2.7 A_partner_100.py
		retStatus=$?
		exit $retStatus
        else
                exit 10 #controllare chmod....
        fi
else
	exit 11 #il programma non esiste
fi
#
