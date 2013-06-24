SET TRIMOUT ON
SET TRIMSPOOL ON
SET TERMOUT ON
SET PAGESIZE 80
SET HEADING ON
SET ECHO OFF
SET TIME ON
SET TIMING ON
SET VERIFY OFF
SET PAUSE OFF
SET FEEDBACK ON
SET ARRAYSIZE 5000
SET LINESIZE 200
SET FLUSH OFF
SET SERVEROUT ON

/*

   Script    crea_job_prepa_addresses.sql
   Creato il 18.06.2012
   Da        Massimiliano Castagno
   Versione  1.0
   Scopo     Script per la creazione di un job di collaudo
   Parametri N/A

   Modifiche 18.06.2012 MCastagno
                        Creazione


*/

WHENEVER OSERROR  CONTINUE
WHENEVER SQLERROR CONTINUE

SPOOL crea_job_prepa_addresses.log

PROMPT Definizione job

PROMPT Definizione variabili

VARIABLE sv_Job_Id VARCHAR2(30)

BEGIN

   :sv_Job_id := 'EXP_ANAGRAFICA_SAP';

   DBMS_OUTPUT.PUT_LINE('Job: ' || :sv_Job_Id);

END;
/

PROMPT svuotamnto tabelle

DELETE
  FROM Wpl_Job_Step_Dep_Registry
 WHERE Job_Id = :sv_Job_id
/

DELETE
  FROM Wpl_Job_Step_Registry
 WHERE Job_Id = :sv_Job_id
/

DELETE
  FROM Wpl_Job_Registry
 WHERE Job_Id = :sv_Job_id
/

-- PROMPT Job_Setup

INSERT
  INTO Wpl_Job_Registry
     (
       Job_Id
     , Executors_Max_Number
     , Version
     , Session_Profile_Id
     , Description
     , Job_Command_Shell
     , Job_Group_Id
     , Notification_Group
     , Notification_Media
     )
VALUES
     (
       :sv_Job_id
     , 4
     , 1
     , 'STANDARD'
     , 'Job Esecuzione aggregazione anagrafica'
     , 'exec_EXP_ANAGRAFICA_SAP.sh'
     , 'Export SAP'
     , 'NONE' 
     , 'MAIL'
     )
/

COMMIT;

-- Inserimento steps

BEGIN

   INSERT
     INTO Wpl_Job_Step_Registry
        (
          Job_Id
        , Step_Id
        , Operation_Id
        , Operation_Order
        , Step_Requirement
        , Maximum_Retry_Number
        , Version
        , Step_Type
        , Command
        , On_Error_Step_Type
        , On_Error_Command
        , Session_Profile_Id
        , Description
        )
   VALUES
        (
          :sv_Job_id -- Job_Id
        , TRIM(UPPER('A_Adrcity'))  --Step_Id
        , TRIM(UPPER('A_Adrcity')) -- Operation_Id
        , 10 -- Operation_Order
        , 'MANDATORY' -- Step_Requirement
        , 2 -- Maximum_Retry_Number
        , 1 -- Version
        , Wpl_Process_Launcher.c_Task_Type_Os_Shell_Native -- Step_Type
        , TRIM('sudo -u sap_user -i /home/sap_user/scripts/A_Adrcity.sh') --- Command
        , NULL -- On_Error_Step_Type
        , NULL -- On_Error_Command
        , 'STANDARD' -- Session_Profile_Id
        , 'Esecuzione A_Adrcity.sh'
        );

   INSERT
     INTO Wpl_Job_Step_Registry
        (
          Job_Id
        , Step_Id
        , Operation_Id
        , Operation_Order
        , Step_Requirement
        , Maximum_Retry_Number
        , Version
        , Step_Type
        , Command
        , On_Error_Step_Type
        , On_Error_Command
        , Session_Profile_Id
        , Description
        )
   VALUES
        (
          :sv_Job_id -- Job_Id
        , TRIM(UPPER('A_Adrstreet'))  --Step_Id
        , TRIM(UPPER('A_Adrstreet')) -- Operation_Id
        , 10 -- Operation_Order
        , 'MANDATORY' -- Step_Requirement
        , 2 -- Maximum_Retry_Number
        , 1 -- Version
        , Wpl_Process_Launcher.c_Task_Type_Os_Shell_Native -- Step_Type
        , TRIM('sudo -u sap_user -i /home/sap_user/scripts/A_Adrstreet.sh') --- Command
        , NULL -- On_Error_Step_Type
        , NULL -- On_Error_Command
        , 'STANDARD' -- Session_Profile_Id
        , 'Esecuzione A_Adrstreet.sh'
        );

/*   INSERT
     INTO Wpl_Job_Step_Registry
        (
          Job_Id
        , Step_Id
        , Operation_Id
        , Operation_Order
        , Step_Requirement
        , Maximum_Retry_Number
        , Version
        , Step_Type
        , Command
        , On_Error_Step_Type
        , On_Error_Command
        , Session_Profile_Id
        , Description
        )
   VALUES
        (
          :sv_Job_id -- Job_Id
        , TRIM(UPPER('E_connobj_030'))  --Step_Id
        , TRIM(UPPER('E_connobj_030')) -- Operation_Id
        , 10 -- Operation_Order
        , 'MANDATORY' -- Step_Requirement
        , 2 -- Maximum_Retry_Number
        , 1 -- Version
        , Wpl_Process_Launcher.c_Task_Type_Os_Shell_Native -- Step_Type
        , TRIM('sudo -u sap_user -i /home/sap_user/scripts/E_connobj_030.sh') --- Command
        , NULL -- On_Error_Step_Type
        , NULL -- On_Error_Command
        , 'STANDARD' -- Session_Profile_Id
        , 'Esecuzione E_connobj_030.sh'
        );*/
--Se non ci sono dipendenze commentare da QUI
/*   INSERT
     INTO Wpl_Job_Step_Dep_Registry
        (
          Job_Id
        , Step_Id
        , Parent_Step_Id
        )
   VALUES
        (
          :sv_Job_id -- Job_Id
        , TRIM(UPPER('E_connobj_030'))  --Step_Id
        , TRIM(UPPER('A_connobj_030'))  -- Parent_Step_Id
        );*/
--A qui
END;
/

COMMIT
/

EXECUTE DBMS_STATS.GATHER_TABLE_STATS(USER, TRIM('WPL_JOB_REGISTRY         '), NULL, 100)
EXECUTE DBMS_STATS.GATHER_TABLE_STATS(USER, TRIM('WPL_JOB_STEP_REGISTRY    '), NULL, 100)
EXECUTE DBMS_STATS.GATHER_TABLE_STATS(USER, TRIM('WPL_JOB_STEP_DEP_REGISTRY'), NULL, 100)
EXECUTE DBMS_STATS.GATHER_TABLE_STATS(USER, TRIM('WPL_JOB_QUEUE            '), NULL, 100)
EXECUTE DBMS_STATS.GATHER_TABLE_STATS(USER, TRIM('WPL_JOB_STEP_QUEUE       '), NULL, 100)
EXECUTE DBMS_STATS.GATHER_TABLE_STATS(USER, TRIM('WPL_JOB_STEP_DEP_QUEUE   '), NULL, 100)
EXECUTE DBMS_STATS.GATHER_TABLE_STATS(USER, TRIM('WPL_TASK_QUEUE           '), NULL, 100)


WHENEVER OSERROR  CONTINUE
WHENEVER SQLERROR CONTINUE

SPOOL OFF


