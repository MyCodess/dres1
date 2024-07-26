Test Case Templ.
========================================================

#####  ==========  Test Case Details:
Project :   RDS-Clearing-Integration-Test  
---------------------------------------------

1. **Test Case Name**  :  Loader-Account-Validation--RDS-Integration-Test  
1. **Test Case ID**  :  RDS-TCase.0021--IntegTest-Loader-Sec (2DO: uniformed aggreed ID assignments)  
1. **Test Case Goal**  :  
    - Validating of the Securities loaded by the RDS-Daily-Loader into RDS-Clearing from Eurex-Classics through the CIL-Interface.  
    - Only Positive-Testing: Are the enriched Account-data read from CIL-interface identical to the data entered into RDS-RefData-DB (considering also the appropriate adaptions based on RDS-Model-Overview)?  
1. **Success Criteria**  :  
    - number of securities entered in the DB and existing in enriched-encoded-files (GPB) is identical.  
    - data contens are identical, except following adaptions :  (2add: mention adaptions AND also the references/links to the spces/UML-Object-Modell/...)  
1. **Pre-Requirements/  Environment Setup**  :  
    - RDS-ENV is setup properly and all application servers are running, as JBOSS, MySql, AMQP, ... (2add: link to RDS-ENV-Setup in WiKi)  
    - RDS-RefData-DB was initially empty (only static data: install+uninstall_db.sh ...)!  
    - RDS-Daily-Loader was started and ended successfully!  
    - The same GPB encoded enriched files for securities are accessible to this test application! (2add: link to the location, where they are expected)  
    - The test is carried out on a standard RDS-ENV plattform!  
1. **Test Tools**  :  
    - besides standard RDS-build-tools (maven, app-servers,...), also:  
    - Google Protocol Buffers (GPB) environment (2add: links to its description)  
1. **Test Data**  :  GPB enriched encoded Account file from CIL-interface: Account64_enriched.enc  
1. **Test Startup Procedure**  :  in the above ENV just call: mvn chek-loader-sec-validity  
1. **Test Closedown Procedure,  Test Outputs,   Test Deliverables**  :  will be ended automatically after finishing the maven task.  
1. **Test Reset Procedure for a Rerun**  :  
    - this test can be repeated /rerun without limitations so long as no new data are loaded into the DB.  
    - this test does NOT change any input or target data!  
    - for a full rerun reset the RefData-DB (uninstall+install_db.sh); restart the application servers, fill the messaging queues with the Account64_enriched.enc date (see wiki-link) and restart the loader again. (2add: link to daily-loader-restart-doc)  
1. **Actor**  :  
    - automated test procedure, implemented as a maven task  
    - also can be invoked manually as (in the above test env) as: "mvn chek-loader-sec-validity"  
    - the automation of the process is to be done/monitored by Jenkins/Cronjobs/... simply by invoking the above maven task!  
1. **External Docs /References**  :  [Loader Specs for Account](to-be-set)  
1. **UML / Object Modell Refs**  :  [Account Entity](to-be-set)  
1. **Risks, Contingencies**  :  
______________________________________________________________________________


#####  ==========  Steps / Protocol:
Step No.**  :  Step Action | Expected Results | Actual Results  
------------------------------------------------------------------
- 01 / start**  :  mvn chek-loader-sec-validity  |
    - generating the log file tcase-0021-loader-sec-test.log  
    - running tests : successfull runs: 63 , failed: 0 , warning < 2
- ...

______________________________________________________________________________


#####  ==========  Additionla Notes:
- ...
- ...
______________________________________________________________________________


