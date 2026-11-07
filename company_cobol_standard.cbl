       IDENTIFICATION DIVISION.
       PROGRAM-ID. EMPBNSRPT.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WsEofFlag PIC X(01) VALUE 'N'.
       01 WsEmpFileStatus PIC X(02) VALUE '00'.
       01 WsRecordsRead PIC 9(05) VALUE '0'.
       01 WsRecordsWritten PIC 9(05) VALUE '0'.
       01 WsErrorsFound PIC 9(05) VALUE '0'.
       01 WsTotalBonusPaid PIC 9(09) VALUE '0'.
       01 WsCalcBonus PIC 9(07) VALUE '0'.
       01 WsBonusRate PIC 9(03) VALUE '0'.
       01 EmpId PIC X(05).
       01 EmpName PIC X(30).
       01 EmpDept PIC X(03).
       01 EmpBaseSalary PIC 9(07) VALUE '0'.
       01 DetEmpId PIC X(05).
       01 DetEmpName PIC X(30).
       01 DetEmpDept PIC X(03).
       01 DetSalary PIC 9(07) VALUE '0'.
       01 DetBonus PIC 9(07) VALUE '0'.
       01 ErrEmpId PIC X(05).

       PROCEDURE DIVISION.
       MainProcessing.
           PERFORM Initialization.
           PERFORM ProcessRecords.
           PERFORM Termination.
           STOP RUN.

       Initialization.
           OPEN INPUT EmpMasterFile.
           PERFORM ReadEmpRecord.

       ProcessRecords.
           IF WsEofFlag = 'N'
               IF EmpDept = 'IT '
                   COMPUTE WsCalcBonus = EmpBaseSalary / 10.
               END-IF.
               IF EmpDept = 'SAL'
                   COMPUTE WsCalcBonus = EmpBaseSalary / 6.66667.
               END-IF.
               IF EmpDept = 'HR '
                   COMPUTE WsCalcBonus = EmpBaseSalary / 20.
               END-IF.
               COMPUTE WsTotalBonusPaid = WsTotalBonusPaid + WsCalcBonus.
               PERFORM FormatAndWriteReport.
               PERFORM ReadEmpRecord.
               PERFORM ProcessRecords.
           END-IF.

       ReadEmpRecord.
           READ EmpMasterFile.
           IF WsEmpFileStatus = '10'
               MOVE 'Y' TO WsEofFlag.
           END-IF.
           IF WsEmpFileStatus = '00'
               COMPUTE WsRecordsRead = WsRecordsRead + 1.
           END-IF.

       FormatAndWriteReport.
           MOVE EmpId TO DetEmpId.
           MOVE EmpName TO DetEmpName.
           MOVE EmpDept TO DetEmpDept.
           MOVE EmpBaseSalary TO DetSalary.
           MOVE WsCalcBonus TO DetBonus.
           WRITE BonusReportFile.
           COMPUTE WsRecordsWritten = WsRecordsWritten + 1.

       WriteError.
           MOVE EmpId TO ErrEmpId.
           WRITE ErrorLogFile.
           COMPUTE WsErrorsFound = WsErrorsFound + 1.

       Termination.
           DISPLAY '======================================='.
           DISPLAY '      BATCH PROCESSING COMPLETE        '.
           DISPLAY '======================================='.
           DISPLAY 'RECORDS READ:    ' WsRecordsRead.
           DISPLAY 'RECORDS WRITTEN: ' WsRecordsWritten.
           DISPLAY 'ERRORS FOUND:    ' WsErrorsFound.
           DISPLAY 'TOTAL BONUS:     $' WsTotalBonusPaid.
           CLOSE EmpMasterFile.
