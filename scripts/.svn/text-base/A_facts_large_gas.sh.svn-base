#Creanetwork S.r.l. g.coppola 12.04.2013                                       #
#------------------------------------------------------------------------------------#
cd $PY_PROGRAMS
#
if [ -f A_facts_Gas_Large.py ]
then
        if [ -x A_facts_Gas_Large.py  ]
        then
                python2.7 A_facts_Gas_Large.py 
                retStatus=$?
                exit $retStatus
        else
                exit 10 #controllare chmod....
        fi
else
        exit 11 #il programma non esiste
fi
#

