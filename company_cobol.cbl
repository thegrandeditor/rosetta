       IDENTIFICATION DIVISION.
       PROGRAM-ID.    EMP-BNS-RPT.
       AUTHOR.        ENTERPRISE-DEV-TEAM.
       DATE-WRITTEN.  2026-05-24.
       SECURITY.      CONFIDENTIAL.
      *----------------------------------------------------------------*
      * PROGRAM PURPOSE:                                               *
      * READS EMPLOYEE MASTER FILE, CALCULATES YEAR-END BONUS BASED    *
      * ON DEPARTMENT, AND WRITES A FORMATTED PAYROLL REPORT.          *
      * INVALID RECORDS ARE WRITTEN TO AN ERROR LOG.                   *
      *----------------------------------------------------------------*

       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT EMP-MASTER-FILE 
               ASSIGN TO EMPMAST
               ORGANIZATION IS SEQUENTIAL
               FILE STATUS IS WS-EMP-FILE-STATUS.
               
           SELECT BONUS-REPORT-FILE 
               ASSIGN TO BNSRPT
               ORGANIZATION IS SEQUENTIAL
               FILE STATUS IS WS-RPT-FILE-STATUS.

           SELECT ERROR-LOG-FILE
               ASSIGN TO ERRLOG
               ORGANIZATION IS SEQUENTIAL
               FILE STATUS IS WS-ERR-FILE-STATUS.

       DATA DIVISION.
       FILE SECTION.
       FD  EMP-MASTER-FILE
           RECORD CONTAINS 80 CHARACTERS.
       01  EMP-REC.
           05 EMP-ID               PIC X(05).
           05 EMP-NAME             PIC X(30).
           05 EMP-DEPT             PIC X(03).
           05 EMP-BASE-SALARY      PIC 9(07)V99.
           05 FILLER               PIC X(33).

       FD  BONUS-REPORT-FILE
           RECORD CONTAINS 132 CHARACTERS.
       01  RPT-REC                 PIC X(132).

       FD  ERROR-LOG-FILE
           RECORD CONTAINS 80 CHARACTERS.
       01  ERR-REC                 PIC X(80).

       WORKING-STORAGE SECTION.
      *----------------------------------------------------------------*
      * 01 LEVEL - SYSTEM FLAGS AND SWITCHES                           *
      *----------------------------------------------------------------*
       01  WS-SWITCHES.
           05  WS-EOF-FLAG         PIC X(01) VALUE 'N'.
               88  END-OF-FILE               VALUE 'Y'.
               88  NOT-END-OF-FILE           VALUE 'N'.

       01  WS-FILE-STATUS-CODES.
           05  WS-EMP-FILE-STATUS  PIC X(02) VALUE '00'.
               88  EMP-FILE-OK               VALUE '00'.
               88  EMP-FILE-EOF              VALUE '10'.
           05  WS-RPT-FILE-STATUS  PIC X(02) VALUE '00'.
           05  WS-ERR-FILE-STATUS  PIC X(02) VALUE '00'.

      *----------------------------------------------------------------*
      * 01 LEVEL - ACCUMULATORS AND COUNTERS (USING COMP-3)            *
      *----------------------------------------------------------------*
       01  WS-COUNTERS.
           05  WS-RECORDS-READ     PIC S9(05) COMP-3 VALUE ZERO.
           05  WS-RECORDS-WRITTEN  PIC S9(05) COMP-3 VALUE ZERO.
           05  WS-ERRORS-FOUND     PIC S9(05) COMP-3 VALUE ZERO.
           05  WS-TOTAL-BONUS-PAID PIC S9(09)V99 COMP-3 VALUE ZERO.

      *----------------------------------------------------------------*
      * 01 LEVEL - CALCULATION VARIABLES                               *
      *----------------------------------------------------------------*
       01  WS-CALCULATIONS.
           05  WS-CALC-BONUS       PIC 9(07)V99 VALUE ZERO.
           05  WS-BONUS-RATE       PIC V999 VALUE ZERO.

      *----------------------------------------------------------------*
      * 01 LEVEL - REPORT FORMATTING AREAS                             *
      *----------------------------------------------------------------*
       01  WS-DETAIL-LINE.
           05  FILLER              PIC X(05) VALUE SPACES.
           05  DET-EMP-ID          PIC X(05).
           05  FILLER              PIC X(05) VALUE SPACES.
           05  DET-EMP-NAME        PIC X(30).
           05  FILLER              PIC X(05) VALUE SPACES.
           05  DET-EMP-DEPT        PIC X(03).
           05  FILLER              PIC X(05) VALUE SPACES.
           05  DET-SALARY          PIC $$$,$$$,$$9.99.
           05  FILLER              PIC X(05) VALUE SPACES.
           05  DET-BONUS           PIC $$$,$$$,$$9.99.
           05  FILLER              PIC X(45) VALUE SPACES.

       01  WS-ERROR-LINE.
           05  ERR-MSG             PIC X(20) VALUE 'INVALID DEPARTMENT: '.
           05  ERR-EMP-ID          PIC X(05).
           05  FILLER              PIC X(55) VALUE SPACES.

       PROCEDURE DIVISION.
      *----------------------------------------------------------------*
      * MAIN CONTROL STRUCTURE                                         *
      *----------------------------------------------------------------*
       0000-MAIN-PROCESSING.
           PERFORM 1000-INITIALIZATION
           
           PERFORM 2000-PROCESS-RECORDS
               UNTIL END-OF-FILE
               
           PERFORM 3000-TERMINATION
           
           STOP RUN.

      *----------------------------------------------------------------*
      * OPEN FILES AND PERFORM FIRST READ                              *
      *----------------------------------------------------------------*
       1000-INITIALIZATION.
           OPEN INPUT  EMP-MASTER-FILE
                OUTPUT BONUS-REPORT-FILE
                OUTPUT ERROR-LOG-FILE
                
           IF NOT EMP-FILE-OK
               DISPLAY 'FATAL ERROR: CANNOT OPEN EMPLOYEE FILE'
               DISPLAY 'FILE STATUS: ' WS-EMP-FILE-STATUS
               PERFORM 3000-TERMINATION
               STOP RUN
           END-IF

           PERFORM 2100-READ-EMP-RECORD.

      *----------------------------------------------------------------*
      * CORE BUSINESS LOGIC PER RECORD                                 *
      *----------------------------------------------------------------*
       2000-PROCESS-RECORDS.
           EVALUATE EMP-DEPT
               WHEN 'IT '
                   MOVE .10 TO WS-BONUS-RATE
               WHEN 'SAL'
                   MOVE .15 TO WS-BONUS-RATE
               WHEN 'HR '
                   MOVE .05 TO WS-BONUS-RATE
               WHEN OTHER
                   PERFORM 8000-WRITE-ERROR
                   GO TO 2000-PROCESS-EXIT
           END-EVALUATE

           COMPUTE WS-CALC-BONUS ROUNDED = EMP-BASE-SALARY * WS-BONUS-RATE
           ADD WS-CALC-BONUS TO WS-TOTAL-BONUS-PAID

           PERFORM 2200-FORMAT-AND-WRITE-REPORT

           2000-PROCESS-EXIT.
           PERFORM 2100-READ-EMP-RECORD.

      *----------------------------------------------------------------*
      * READ SUBROUTINE                                                *
      *----------------------------------------------------------------*
       2100-READ-EMP-RECORD.
           READ EMP-MASTER-FILE
               AT END
                   SET END-OF-FILE TO TRUE
               NOT AT END
                   ADD 1 TO WS-RECORDS-READ
           END-READ.

      *----------------------------------------------------------------*
      * WRITE REPORT SUBROUTINE                                        *
      *----------------------------------------------------------------*
       2200-FORMAT-AND-WRITE-REPORT.
           INITIALIZE WS-DETAIL-LINE
           MOVE EMP-ID          TO DET-EMP-ID
           MOVE EMP-NAME        TO DET-EMP-NAME
           MOVE EMP-DEPT        TO DET-EMP-DEPT
           MOVE EMP-BASE-SALARY TO DET-SALARY
           MOVE WS-CALC-BONUS   TO DET-BONUS
           
           WRITE RPT-REC FROM WS-DETAIL-LINE
           ADD 1 TO WS-RECORDS-WRITTEN.

      *----------------------------------------------------------------*
      * ERROR HANDLING                                                 *
      *----------------------------------------------------------------*
       8000-WRITE-ERROR.
           MOVE EMP-ID TO ERR-EMP-ID
           WRITE ERR-REC FROM WS-ERROR-LINE
           ADD 1 TO WS-ERRORS-FOUND.

      *----------------------------------------------------------------*
      * CLEANUP AND CLOSEOUT                                           *
      *----------------------------------------------------------------*
       3000-TERMINATION.
           DISPLAY '======================================='
           DISPLAY '      BATCH PROCESSING COMPLETE        '
           DISPLAY '======================================='
           DISPLAY 'RECORDS READ:    ' WS-RECORDS-READ
           DISPLAY 'RECORDS WRITTEN: ' WS-RECORDS-WRITTEN
           DISPLAY 'ERRORS FOUND:    ' WS-ERRORS-FOUND
           DISPLAY 'TOTAL BONUS:     $' WS-TOTAL-BONUS-PAID
           
           CLOSE EMP-MASTER-FILE
                 BONUS-REPORT-FILE
                 ERROR-LOG-FILE.
