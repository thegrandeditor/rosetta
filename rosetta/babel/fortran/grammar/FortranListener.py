# Generated from rosetta/babel/fortran/grammar/Fortran.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .FortranParser import FortranParser
else:
    from FortranParser import FortranParser

# This class defines a complete listener for a parse tree produced by FortranParser.
class FortranListener(ParseTreeListener):

    # Enter a parse tree produced by FortranParser#program.
    def enterProgram(self, ctx:FortranParser.ProgramContext):
        pass

    # Exit a parse tree produced by FortranParser#program.
    def exitProgram(self, ctx:FortranParser.ProgramContext):
        pass


    # Enter a parse tree produced by FortranParser#executable_unit.
    def enterExecutable_unit(self, ctx:FortranParser.Executable_unitContext):
        pass

    # Exit a parse tree produced by FortranParser#executable_unit.
    def exitExecutable_unit(self, ctx:FortranParser.Executable_unitContext):
        pass


    # Enter a parse tree produced by FortranParser#main_program.
    def enterMain_program(self, ctx:FortranParser.Main_programContext):
        pass

    # Exit a parse tree produced by FortranParser#main_program.
    def exitMain_program(self, ctx:FortranParser.Main_programContext):
        pass


    # Enter a parse tree produced by FortranParser#subroutine_def.
    def enterSubroutine_def(self, ctx:FortranParser.Subroutine_defContext):
        pass

    # Exit a parse tree produced by FortranParser#subroutine_def.
    def exitSubroutine_def(self, ctx:FortranParser.Subroutine_defContext):
        pass


    # Enter a parse tree produced by FortranParser#function_def.
    def enterFunction_def(self, ctx:FortranParser.Function_defContext):
        pass

    # Exit a parse tree produced by FortranParser#function_def.
    def exitFunction_def(self, ctx:FortranParser.Function_defContext):
        pass


    # Enter a parse tree produced by FortranParser#program_stmt.
    def enterProgram_stmt(self, ctx:FortranParser.Program_stmtContext):
        pass

    # Exit a parse tree produced by FortranParser#program_stmt.
    def exitProgram_stmt(self, ctx:FortranParser.Program_stmtContext):
        pass


    # Enter a parse tree produced by FortranParser#subroutine_stmt.
    def enterSubroutine_stmt(self, ctx:FortranParser.Subroutine_stmtContext):
        pass

    # Exit a parse tree produced by FortranParser#subroutine_stmt.
    def exitSubroutine_stmt(self, ctx:FortranParser.Subroutine_stmtContext):
        pass


    # Enter a parse tree produced by FortranParser#function_stmt.
    def enterFunction_stmt(self, ctx:FortranParser.Function_stmtContext):
        pass

    # Exit a parse tree produced by FortranParser#function_stmt.
    def exitFunction_stmt(self, ctx:FortranParser.Function_stmtContext):
        pass


    # Enter a parse tree produced by FortranParser#end_stmt.
    def enterEnd_stmt(self, ctx:FortranParser.End_stmtContext):
        pass

    # Exit a parse tree produced by FortranParser#end_stmt.
    def exitEnd_stmt(self, ctx:FortranParser.End_stmtContext):
        pass


    # Enter a parse tree produced by FortranParser#specification_part.
    def enterSpecification_part(self, ctx:FortranParser.Specification_partContext):
        pass

    # Exit a parse tree produced by FortranParser#specification_part.
    def exitSpecification_part(self, ctx:FortranParser.Specification_partContext):
        pass


    # Enter a parse tree produced by FortranParser#specification_stmt.
    def enterSpecification_stmt(self, ctx:FortranParser.Specification_stmtContext):
        pass

    # Exit a parse tree produced by FortranParser#specification_stmt.
    def exitSpecification_stmt(self, ctx:FortranParser.Specification_stmtContext):
        pass


    # Enter a parse tree produced by FortranParser#type_declaration_stmt.
    def enterType_declaration_stmt(self, ctx:FortranParser.Type_declaration_stmtContext):
        pass

    # Exit a parse tree produced by FortranParser#type_declaration_stmt.
    def exitType_declaration_stmt(self, ctx:FortranParser.Type_declaration_stmtContext):
        pass


    # Enter a parse tree produced by FortranParser#type_spec.
    def enterType_spec(self, ctx:FortranParser.Type_specContext):
        pass

    # Exit a parse tree produced by FortranParser#type_spec.
    def exitType_spec(self, ctx:FortranParser.Type_specContext):
        pass


    # Enter a parse tree produced by FortranParser#entity_decl.
    def enterEntity_decl(self, ctx:FortranParser.Entity_declContext):
        pass

    # Exit a parse tree produced by FortranParser#entity_decl.
    def exitEntity_decl(self, ctx:FortranParser.Entity_declContext):
        pass


    # Enter a parse tree produced by FortranParser#array_spec.
    def enterArray_spec(self, ctx:FortranParser.Array_specContext):
        pass

    # Exit a parse tree produced by FortranParser#array_spec.
    def exitArray_spec(self, ctx:FortranParser.Array_specContext):
        pass


    # Enter a parse tree produced by FortranParser#dimension.
    def enterDimension(self, ctx:FortranParser.DimensionContext):
        pass

    # Exit a parse tree produced by FortranParser#dimension.
    def exitDimension(self, ctx:FortranParser.DimensionContext):
        pass


    # Enter a parse tree produced by FortranParser#implicit_none_stmt.
    def enterImplicit_none_stmt(self, ctx:FortranParser.Implicit_none_stmtContext):
        pass

    # Exit a parse tree produced by FortranParser#implicit_none_stmt.
    def exitImplicit_none_stmt(self, ctx:FortranParser.Implicit_none_stmtContext):
        pass


    # Enter a parse tree produced by FortranParser#common_stmt.
    def enterCommon_stmt(self, ctx:FortranParser.Common_stmtContext):
        pass

    # Exit a parse tree produced by FortranParser#common_stmt.
    def exitCommon_stmt(self, ctx:FortranParser.Common_stmtContext):
        pass


    # Enter a parse tree produced by FortranParser#dimension_stmt.
    def enterDimension_stmt(self, ctx:FortranParser.Dimension_stmtContext):
        pass

    # Exit a parse tree produced by FortranParser#dimension_stmt.
    def exitDimension_stmt(self, ctx:FortranParser.Dimension_stmtContext):
        pass


    # Enter a parse tree produced by FortranParser#execution_part.
    def enterExecution_part(self, ctx:FortranParser.Execution_partContext):
        pass

    # Exit a parse tree produced by FortranParser#execution_part.
    def exitExecution_part(self, ctx:FortranParser.Execution_partContext):
        pass


    # Enter a parse tree produced by FortranParser#executable_stmt.
    def enterExecutable_stmt(self, ctx:FortranParser.Executable_stmtContext):
        pass

    # Exit a parse tree produced by FortranParser#executable_stmt.
    def exitExecutable_stmt(self, ctx:FortranParser.Executable_stmtContext):
        pass


    # Enter a parse tree produced by FortranParser#action_stmt.
    def enterAction_stmt(self, ctx:FortranParser.Action_stmtContext):
        pass

    # Exit a parse tree produced by FortranParser#action_stmt.
    def exitAction_stmt(self, ctx:FortranParser.Action_stmtContext):
        pass


    # Enter a parse tree produced by FortranParser#assignment_stmt.
    def enterAssignment_stmt(self, ctx:FortranParser.Assignment_stmtContext):
        pass

    # Exit a parse tree produced by FortranParser#assignment_stmt.
    def exitAssignment_stmt(self, ctx:FortranParser.Assignment_stmtContext):
        pass


    # Enter a parse tree produced by FortranParser#if_stmt.
    def enterIf_stmt(self, ctx:FortranParser.If_stmtContext):
        pass

    # Exit a parse tree produced by FortranParser#if_stmt.
    def exitIf_stmt(self, ctx:FortranParser.If_stmtContext):
        pass


    # Enter a parse tree produced by FortranParser#do_stmt.
    def enterDo_stmt(self, ctx:FortranParser.Do_stmtContext):
        pass

    # Exit a parse tree produced by FortranParser#do_stmt.
    def exitDo_stmt(self, ctx:FortranParser.Do_stmtContext):
        pass


    # Enter a parse tree produced by FortranParser#goto_stmt.
    def enterGoto_stmt(self, ctx:FortranParser.Goto_stmtContext):
        pass

    # Exit a parse tree produced by FortranParser#goto_stmt.
    def exitGoto_stmt(self, ctx:FortranParser.Goto_stmtContext):
        pass


    # Enter a parse tree produced by FortranParser#call_stmt.
    def enterCall_stmt(self, ctx:FortranParser.Call_stmtContext):
        pass

    # Exit a parse tree produced by FortranParser#call_stmt.
    def exitCall_stmt(self, ctx:FortranParser.Call_stmtContext):
        pass


    # Enter a parse tree produced by FortranParser#return_stmt.
    def enterReturn_stmt(self, ctx:FortranParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by FortranParser#return_stmt.
    def exitReturn_stmt(self, ctx:FortranParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by FortranParser#write_stmt.
    def enterWrite_stmt(self, ctx:FortranParser.Write_stmtContext):
        pass

    # Exit a parse tree produced by FortranParser#write_stmt.
    def exitWrite_stmt(self, ctx:FortranParser.Write_stmtContext):
        pass


    # Enter a parse tree produced by FortranParser#print_stmt.
    def enterPrint_stmt(self, ctx:FortranParser.Print_stmtContext):
        pass

    # Exit a parse tree produced by FortranParser#print_stmt.
    def exitPrint_stmt(self, ctx:FortranParser.Print_stmtContext):
        pass


    # Enter a parse tree produced by FortranParser#format_stmt.
    def enterFormat_stmt(self, ctx:FortranParser.Format_stmtContext):
        pass

    # Exit a parse tree produced by FortranParser#format_stmt.
    def exitFormat_stmt(self, ctx:FortranParser.Format_stmtContext):
        pass


    # Enter a parse tree produced by FortranParser#format_item.
    def enterFormat_item(self, ctx:FortranParser.Format_itemContext):
        pass

    # Exit a parse tree produced by FortranParser#format_item.
    def exitFormat_item(self, ctx:FortranParser.Format_itemContext):
        pass


    # Enter a parse tree produced by FortranParser#label.
    def enterLabel(self, ctx:FortranParser.LabelContext):
        pass

    # Exit a parse tree produced by FortranParser#label.
    def exitLabel(self, ctx:FortranParser.LabelContext):
        pass


    # Enter a parse tree produced by FortranParser#identifier.
    def enterIdentifier(self, ctx:FortranParser.IdentifierContext):
        pass

    # Exit a parse tree produced by FortranParser#identifier.
    def exitIdentifier(self, ctx:FortranParser.IdentifierContext):
        pass


    # Enter a parse tree produced by FortranParser#expression.
    def enterExpression(self, ctx:FortranParser.ExpressionContext):
        pass

    # Exit a parse tree produced by FortranParser#expression.
    def exitExpression(self, ctx:FortranParser.ExpressionContext):
        pass


    # Enter a parse tree produced by FortranParser#primary.
    def enterPrimary(self, ctx:FortranParser.PrimaryContext):
        pass

    # Exit a parse tree produced by FortranParser#primary.
    def exitPrimary(self, ctx:FortranParser.PrimaryContext):
        pass


    # Enter a parse tree produced by FortranParser#literal.
    def enterLiteral(self, ctx:FortranParser.LiteralContext):
        pass

    # Exit a parse tree produced by FortranParser#literal.
    def exitLiteral(self, ctx:FortranParser.LiteralContext):
        pass


    # Enter a parse tree produced by FortranParser#integer_literal.
    def enterInteger_literal(self, ctx:FortranParser.Integer_literalContext):
        pass

    # Exit a parse tree produced by FortranParser#integer_literal.
    def exitInteger_literal(self, ctx:FortranParser.Integer_literalContext):
        pass


    # Enter a parse tree produced by FortranParser#real_literal.
    def enterReal_literal(self, ctx:FortranParser.Real_literalContext):
        pass

    # Exit a parse tree produced by FortranParser#real_literal.
    def exitReal_literal(self, ctx:FortranParser.Real_literalContext):
        pass


    # Enter a parse tree produced by FortranParser#string_literal.
    def enterString_literal(self, ctx:FortranParser.String_literalContext):
        pass

    # Exit a parse tree produced by FortranParser#string_literal.
    def exitString_literal(self, ctx:FortranParser.String_literalContext):
        pass


    # Enter a parse tree produced by FortranParser#logical_literal.
    def enterLogical_literal(self, ctx:FortranParser.Logical_literalContext):
        pass

    # Exit a parse tree produced by FortranParser#logical_literal.
    def exitLogical_literal(self, ctx:FortranParser.Logical_literalContext):
        pass



del FortranParser