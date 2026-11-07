# Generated from Cobol.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CobolParser import CobolParser
else:
    from CobolParser import CobolParser

# This class defines a complete listener for a parse tree produced by CobolParser.
class CobolListener(ParseTreeListener):

    # Enter a parse tree produced by CobolParser#program.
    def enterProgram(self, ctx:CobolParser.ProgramContext):
        pass

    # Exit a parse tree produced by CobolParser#program.
    def exitProgram(self, ctx:CobolParser.ProgramContext):
        pass


    # Enter a parse tree produced by CobolParser#copyStatement.
    def enterCopyStatement(self, ctx:CobolParser.CopyStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#copyStatement.
    def exitCopyStatement(self, ctx:CobolParser.CopyStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#identificationDivision.
    def enterIdentificationDivision(self, ctx:CobolParser.IdentificationDivisionContext):
        pass

    # Exit a parse tree produced by CobolParser#identificationDivision.
    def exitIdentificationDivision(self, ctx:CobolParser.IdentificationDivisionContext):
        pass


    # Enter a parse tree produced by CobolParser#identificationEntry.
    def enterIdentificationEntry(self, ctx:CobolParser.IdentificationEntryContext):
        pass

    # Exit a parse tree produced by CobolParser#identificationEntry.
    def exitIdentificationEntry(self, ctx:CobolParser.IdentificationEntryContext):
        pass


    # Enter a parse tree produced by CobolParser#identificationValue.
    def enterIdentificationValue(self, ctx:CobolParser.IdentificationValueContext):
        pass

    # Exit a parse tree produced by CobolParser#identificationValue.
    def exitIdentificationValue(self, ctx:CobolParser.IdentificationValueContext):
        pass


    # Enter a parse tree produced by CobolParser#programName.
    def enterProgramName(self, ctx:CobolParser.ProgramNameContext):
        pass

    # Exit a parse tree produced by CobolParser#programName.
    def exitProgramName(self, ctx:CobolParser.ProgramNameContext):
        pass


    # Enter a parse tree produced by CobolParser#environmentDivision.
    def enterEnvironmentDivision(self, ctx:CobolParser.EnvironmentDivisionContext):
        pass

    # Exit a parse tree produced by CobolParser#environmentDivision.
    def exitEnvironmentDivision(self, ctx:CobolParser.EnvironmentDivisionContext):
        pass


    # Enter a parse tree produced by CobolParser#inputOutputSection.
    def enterInputOutputSection(self, ctx:CobolParser.InputOutputSectionContext):
        pass

    # Exit a parse tree produced by CobolParser#inputOutputSection.
    def exitInputOutputSection(self, ctx:CobolParser.InputOutputSectionContext):
        pass


    # Enter a parse tree produced by CobolParser#fileControl.
    def enterFileControl(self, ctx:CobolParser.FileControlContext):
        pass

    # Exit a parse tree produced by CobolParser#fileControl.
    def exitFileControl(self, ctx:CobolParser.FileControlContext):
        pass


    # Enter a parse tree produced by CobolParser#selectStatement.
    def enterSelectStatement(self, ctx:CobolParser.SelectStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#selectStatement.
    def exitSelectStatement(self, ctx:CobolParser.SelectStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#selectClause.
    def enterSelectClause(self, ctx:CobolParser.SelectClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#selectClause.
    def exitSelectClause(self, ctx:CobolParser.SelectClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#dataDivision.
    def enterDataDivision(self, ctx:CobolParser.DataDivisionContext):
        pass

    # Exit a parse tree produced by CobolParser#dataDivision.
    def exitDataDivision(self, ctx:CobolParser.DataDivisionContext):
        pass


    # Enter a parse tree produced by CobolParser#fileSection.
    def enterFileSection(self, ctx:CobolParser.FileSectionContext):
        pass

    # Exit a parse tree produced by CobolParser#fileSection.
    def exitFileSection(self, ctx:CobolParser.FileSectionContext):
        pass


    # Enter a parse tree produced by CobolParser#fileDescriptionEntry.
    def enterFileDescriptionEntry(self, ctx:CobolParser.FileDescriptionEntryContext):
        pass

    # Exit a parse tree produced by CobolParser#fileDescriptionEntry.
    def exitFileDescriptionEntry(self, ctx:CobolParser.FileDescriptionEntryContext):
        pass


    # Enter a parse tree produced by CobolParser#fdClause.
    def enterFdClause(self, ctx:CobolParser.FdClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#fdClause.
    def exitFdClause(self, ctx:CobolParser.FdClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#workingStorageSection.
    def enterWorkingStorageSection(self, ctx:CobolParser.WorkingStorageSectionContext):
        pass

    # Exit a parse tree produced by CobolParser#workingStorageSection.
    def exitWorkingStorageSection(self, ctx:CobolParser.WorkingStorageSectionContext):
        pass


    # Enter a parse tree produced by CobolParser#linkageSection.
    def enterLinkageSection(self, ctx:CobolParser.LinkageSectionContext):
        pass

    # Exit a parse tree produced by CobolParser#linkageSection.
    def exitLinkageSection(self, ctx:CobolParser.LinkageSectionContext):
        pass


    # Enter a parse tree produced by CobolParser#dataDescriptionEntry.
    def enterDataDescriptionEntry(self, ctx:CobolParser.DataDescriptionEntryContext):
        pass

    # Exit a parse tree produced by CobolParser#dataDescriptionEntry.
    def exitDataDescriptionEntry(self, ctx:CobolParser.DataDescriptionEntryContext):
        pass


    # Enter a parse tree produced by CobolParser#dataClause.
    def enterDataClause(self, ctx:CobolParser.DataClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#dataClause.
    def exitDataClause(self, ctx:CobolParser.DataClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#usageClause.
    def enterUsageClause(self, ctx:CobolParser.UsageClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#usageClause.
    def exitUsageClause(self, ctx:CobolParser.UsageClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#procedureDivision.
    def enterProcedureDivision(self, ctx:CobolParser.ProcedureDivisionContext):
        pass

    # Exit a parse tree produced by CobolParser#procedureDivision.
    def exitProcedureDivision(self, ctx:CobolParser.ProcedureDivisionContext):
        pass


    # Enter a parse tree produced by CobolParser#procedureBody.
    def enterProcedureBody(self, ctx:CobolParser.ProcedureBodyContext):
        pass

    # Exit a parse tree produced by CobolParser#procedureBody.
    def exitProcedureBody(self, ctx:CobolParser.ProcedureBodyContext):
        pass


    # Enter a parse tree produced by CobolParser#paragraph.
    def enterParagraph(self, ctx:CobolParser.ParagraphContext):
        pass

    # Exit a parse tree produced by CobolParser#paragraph.
    def exitParagraph(self, ctx:CobolParser.ParagraphContext):
        pass


    # Enter a parse tree produced by CobolParser#statement.
    def enterStatement(self, ctx:CobolParser.StatementContext):
        pass

    # Exit a parse tree produced by CobolParser#statement.
    def exitStatement(self, ctx:CobolParser.StatementContext):
        pass


    # Enter a parse tree produced by CobolParser#moveStatement.
    def enterMoveStatement(self, ctx:CobolParser.MoveStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#moveStatement.
    def exitMoveStatement(self, ctx:CobolParser.MoveStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#displayStatement.
    def enterDisplayStatement(self, ctx:CobolParser.DisplayStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#displayStatement.
    def exitDisplayStatement(self, ctx:CobolParser.DisplayStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#stopRunStatement.
    def enterStopRunStatement(self, ctx:CobolParser.StopRunStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#stopRunStatement.
    def exitStopRunStatement(self, ctx:CobolParser.StopRunStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#addStatement.
    def enterAddStatement(self, ctx:CobolParser.AddStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#addStatement.
    def exitAddStatement(self, ctx:CobolParser.AddStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#subtractStatement.
    def enterSubtractStatement(self, ctx:CobolParser.SubtractStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#subtractStatement.
    def exitSubtractStatement(self, ctx:CobolParser.SubtractStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#multiplyStatement.
    def enterMultiplyStatement(self, ctx:CobolParser.MultiplyStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#multiplyStatement.
    def exitMultiplyStatement(self, ctx:CobolParser.MultiplyStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#divideStatement.
    def enterDivideStatement(self, ctx:CobolParser.DivideStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#divideStatement.
    def exitDivideStatement(self, ctx:CobolParser.DivideStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#initializeStatement.
    def enterInitializeStatement(self, ctx:CobolParser.InitializeStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#initializeStatement.
    def exitInitializeStatement(self, ctx:CobolParser.InitializeStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#setStatement.
    def enterSetStatement(self, ctx:CobolParser.SetStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#setStatement.
    def exitSetStatement(self, ctx:CobolParser.SetStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#ifStatement.
    def enterIfStatement(self, ctx:CobolParser.IfStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#ifStatement.
    def exitIfStatement(self, ctx:CobolParser.IfStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#performStatement.
    def enterPerformStatement(self, ctx:CobolParser.PerformStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#performStatement.
    def exitPerformStatement(self, ctx:CobolParser.PerformStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#computeStatement.
    def enterComputeStatement(self, ctx:CobolParser.ComputeStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#computeStatement.
    def exitComputeStatement(self, ctx:CobolParser.ComputeStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#evaluateStatement.
    def enterEvaluateStatement(self, ctx:CobolParser.EvaluateStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#evaluateStatement.
    def exitEvaluateStatement(self, ctx:CobolParser.EvaluateStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#whenClause.
    def enterWhenClause(self, ctx:CobolParser.WhenClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#whenClause.
    def exitWhenClause(self, ctx:CobolParser.WhenClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#whenOtherClause.
    def enterWhenOtherClause(self, ctx:CobolParser.WhenOtherClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#whenOtherClause.
    def exitWhenOtherClause(self, ctx:CobolParser.WhenOtherClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#callStatement.
    def enterCallStatement(self, ctx:CobolParser.CallStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#callStatement.
    def exitCallStatement(self, ctx:CobolParser.CallStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#goToStatement.
    def enterGoToStatement(self, ctx:CobolParser.GoToStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#goToStatement.
    def exitGoToStatement(self, ctx:CobolParser.GoToStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#sqlStatement.
    def enterSqlStatement(self, ctx:CobolParser.SqlStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#sqlStatement.
    def exitSqlStatement(self, ctx:CobolParser.SqlStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#fileStatement.
    def enterFileStatement(self, ctx:CobolParser.FileStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#fileStatement.
    def exitFileStatement(self, ctx:CobolParser.FileStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#openPhrase.
    def enterOpenPhrase(self, ctx:CobolParser.OpenPhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#openPhrase.
    def exitOpenPhrase(self, ctx:CobolParser.OpenPhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#condition.
    def enterCondition(self, ctx:CobolParser.ConditionContext):
        pass

    # Exit a parse tree produced by CobolParser#condition.
    def exitCondition(self, ctx:CobolParser.ConditionContext):
        pass


    # Enter a parse tree produced by CobolParser#operator.
    def enterOperator(self, ctx:CobolParser.OperatorContext):
        pass

    # Exit a parse tree produced by CobolParser#operator.
    def exitOperator(self, ctx:CobolParser.OperatorContext):
        pass


    # Enter a parse tree produced by CobolParser#expression.
    def enterExpression(self, ctx:CobolParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CobolParser#expression.
    def exitExpression(self, ctx:CobolParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CobolParser#literal.
    def enterLiteral(self, ctx:CobolParser.LiteralContext):
        pass

    # Exit a parse tree produced by CobolParser#literal.
    def exitLiteral(self, ctx:CobolParser.LiteralContext):
        pass


    # Enter a parse tree produced by CobolParser#specialLiteral.
    def enterSpecialLiteral(self, ctx:CobolParser.SpecialLiteralContext):
        pass

    # Exit a parse tree produced by CobolParser#specialLiteral.
    def exitSpecialLiteral(self, ctx:CobolParser.SpecialLiteralContext):
        pass


    # Enter a parse tree produced by CobolParser#anyNumber.
    def enterAnyNumber(self, ctx:CobolParser.AnyNumberContext):
        pass

    # Exit a parse tree produced by CobolParser#anyNumber.
    def exitAnyNumber(self, ctx:CobolParser.AnyNumberContext):
        pass


    # Enter a parse tree produced by CobolParser#cobolName.
    def enterCobolName(self, ctx:CobolParser.CobolNameContext):
        pass

    # Exit a parse tree produced by CobolParser#cobolName.
    def exitCobolName(self, ctx:CobolParser.CobolNameContext):
        pass



del CobolParser