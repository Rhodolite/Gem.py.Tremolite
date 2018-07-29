#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('TremoliteParser.DualExpressionStatement')
def module():
    class PatternStatement(DualExpressionStatement):
        __slots__    = (())
        display_name = 'pattern-statement'
        frill        = conjure_vwx_frill(empty_indentation, W__COLON_EQUAL__W, LINE_MARKER)


    #
    #   NOTE:
    #       Currently `conjure_pattern_statement__with_frill` -- but it will be in the future, so it is left in here
    #       (rather than refactoring it out).
    #
    [
        conjure_pattern_statement, conjure_pattern_statement__with_frill,
    ] = produce_dual_expression_statement('pattern-statement', PatternStatement)


    share(
        'conjure_pattern_statement',    conjure_pattern_statement
    )
