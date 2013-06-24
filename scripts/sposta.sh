#!/bin/bash
#-----------------------------------------------------------------------------------------#
# 17.01.2013 Creanetwork S.r.l.                                                           #
#            Questo script serve a trasferire un file emigall verso il sistema SAP.       #
#-----------------------------------------------------------------------------------------#

HOST="172.26.90.1"
USER="if-sap"
PASS="sorgenia"
EMIG=$1
#
ADESSO=`date +"%Y%m%d"`
#echo $ADESSO
ARCHIVIO=`ls -t ${EMIGALL_FILES}/${EMIG}_${ADESSO}-*.txt | head -1`
#echo "ARCHIVIO:"${ARCHIVIO}
cp ${ARCHIVIO} /tmp

ARCHIVIO_NETTO=`basename ${ARCHIVIO}`
#echo "ARCHIVIO_NETTO: "${ARCHIVIO_NETTO}

NOME_FILE=`echo ${ARCHIVIO_NETTO}| cut -d "." -f1`
#echo "NOME_FILE     : "${NOME_FILE}
zip  /tmp/${NOME_FILE} /tmp/${ARCHIVIO_NETTO}
echo "inizio trasferimento..."

lftp -u ${USER},${PASS}  sftp://${HOST} <<EOF
cd EMIGALL
lcd ${EMIGALL_FILES}
put  /tmp/${NOME_FILE}.zip
bye
EOF

echo "finito"
