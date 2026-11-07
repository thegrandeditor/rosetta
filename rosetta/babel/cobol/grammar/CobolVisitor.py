# Generated from Cobol.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CobolParser import CobolParser
else:
    from CobolParser import CobolParser

# This class defines a complete generic visitor for a parse tree produced by CobolParser.

class CobolVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CobolParser#program.
    def visitProgram(self, ctx:CobolParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#copyStatement.
    def visitCopyStatement(self, ctx:CobolParser.CopyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#identificationDivision.
    def visitIdentificationDivision(self, ctx:CobolParser.IdentificationDivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#identificationEntry.
    def visitIdentificationEntry(self, ctx:CobolParser.IdentificationEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#identificationValue.
    def visitIdentificationValue(self, ctx:CobolParser.IdentificationValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#programName.
    def visitProgramName(self, ctx:CobolParser.ProgramNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#environmentDivision.
    def visitEnvironmentDivision(self, ctx:CobolParser.EnvironmentDivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#inputOutputSection.
    def visitInputOutputSection(self, ctx:CobolParser.InputOutputSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#fileControl.
    def visitFileControl(self, ctx:CobolParser.FileControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#selectStatement.
    def visitSelectStatement(self, ctx:CobolParser.SelectStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#selectClause.
    def visitSelectClause(self, ctx:CobolParser.SelectClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataDivision.
    def visitDataDivision(self, ctx:CobolParser.DataDivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#fileSection.
    def visitFileSection(self, ctx:CobolParser.FileSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#fileDescriptionEntry.
    def visitFileDescriptionEntry(self, ctx:CobolParser.FileDescriptionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#fdClause.
    def visitFdClause(self, ctx:CobolParser.FdClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#workingStorageSection.
    def visitWorkingStorageSection(self, ctx:CobolParser.WorkingStorageSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#linkageSection.
    def visitLinkageSection(self, ctx:CobolParser.LinkageSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataDescriptionEntry.
    def visitDataDescriptionEntry(self, ctx:CobolParser.DataDescriptionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataClause.
    def visitDataClause(self, ctx:CobolParser.DataClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#usageClause.
    def visitUsageClause(self, ctx:CobolParser.UsageClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#procedureDivision.
    def visitProcedureDivision(self, ctx:CobolParser.ProcedureDivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#procedureBody.
    def visitProcedureBody(self, ctx:CobolParser.ProcedureBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#paragraph.
    def visitParagraph(self, ctx:CobolParser.ParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#statement.
    def visitStatement(self, ctx:CobolParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#moveStatement.
    def visitMoveStatement(self, ctx:CobolParser.MoveStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#displayStatement.
    def visitDisplayStatement(self, ctx:CobolParser.DisplayStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#stopRunStatement.
    def visitStopRunStatement(self, ctx:CobolParser.StopRunStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#addStatement.
    def visitAddStatement(self, ctx:CobolParser.AddStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#subtractStatement.
    def visitSubtractStatement(self, ctx:CobolParser.SubtractStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#multiplyStatement.
    def visitMultiplyStatement(self, ctx:CobolParser.MultiplyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#divideStatement.
    def visitDivideStatement(self, ctx:CobolParser.DivideStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#initializeStatement.
    def visitInitializeStatement(self, ctx:CobolParser.InitializeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#setStatement.
    def visitSetStatement(self, ctx:CobolParser.SetStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#ifStatement.
    def visitIfStatement(self, ctx:CobolParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#performStatement.
    def visitPerformStatement(self, ctx:CobolParser.PerformStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#computeStatement.
    def visitComputeStatement(self, ctx:CobolParser.ComputeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#evaluateStatement.
    def visitEvaluateStatement(self, ctx:CobolParser.EvaluateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#whenClause.
    def visitWhenClause(self, ctx:CobolParser.WhenClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#whenOtherClause.
    def visitWhenOtherClause(self, ctx:CobolParser.WhenOtherClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#callStatement.
    def visitCallStatement(self, ctx:CobolParser.CallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#goToStatement.
    def visitGoToStatement(self, ctx:CobolParser.GoToStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#sqlStatement.
    def visitSqlStatement(self, ctx:CobolParser.SqlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#fileStatement.
    def visitFileStatement(self, ctx:CobolParser.FileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#openPhrase.
    def visitOpenPhrase(self, ctx:CobolParser.OpenPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#condition.
    def visitCondition(self, ctx:CobolParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#operator.
    def visitOperator(self, ctx:CobolParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#expression.
    def visitExpression(self, ctx:CobolParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#literal.
    def visitLiteral(self, ctx:CobolParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#specialLiteral.
    def visitSpecialLiteral(self, ctx:CobolParser.SpecialLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#anyNumber.
    def visitAnyNumber(self, ctx:CobolParser.AnyNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#cobolName.
    def visitCobolName(self, ctx:CobolParser.CobolNameContext):
        return self.visitChildren(ctx)



del CobolParser