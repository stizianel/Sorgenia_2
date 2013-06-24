rge    ------>  Estrattore  Multi Struttura Facts UNICO EMIGALL        #
#   Creanetwork S.r.l. a.rossoni 18.01.2013                                          #
#------------------------------------------------------------------------------------#
cd $PY_PROGRAMS
#
if [ -f E_factsgenLargeGas.py ]
then
        if [ -x E_factsgenLargeGas.py ]
        then
                python2.7 E_factsgenLargeGas.py
                retStatus=$?
                $SH_SCRIPTS/sposta.sh factsgenLargeGas
                exit $retStatus
        else
                exit 10 #controllare chmod....
        fi
else
        exit 11 #il programma non esiste
fi
#

