!/bin/bash
#
#------------------------------------------------------------------------------------#
# E_partner_100    ------>  Estrattore  Struttura Partner                            #
#   Creanetwork S.r.l. a.rossoni 15.11.2012                                          #
#------------------------------------------------------------------------------------#
cd $PY_PROGRAMS
#
if [ -f E_partner_100.py ]
then
        if [ -x E_partner_100.py ]
	then
		python2.7 E_partner_100.py
		retStatus=$?
#                $SH_SCRIPTS/sposta.sh partner
		exit $retStatus
        else
                exit 10 #controllare chmod....
        fi
else
	exit 11 #il programma non esiste
fi
#
