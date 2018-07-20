#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('Tremolite_2.Pattern')
def gem():
    require_gem('Tremolite_2.Core')
    require_gem('Tremolite.Build')
    require_gem('Tremolite.CreateMatch')
    require_gem('Tremolite.Name')


    from Tremolite import create_match_code, ANY_OF, BACKSLASH, DOT, EMPTY, END_OF_PATTERN, EXACT
    from Tremolite import G, LINEFEED, MATCH, NAME, NAMED_GROUP, NOT_ANY_OF, NOT_FOLLOWED_BY
    from Tremolite import ONE_OR_MORE, OPTIONAL, PRINTABLE, PRINTABLE_MINUS, Q, ZERO_OR_MORE


    FULL_MATCH = MATCH
    P          = OPTIONAL


    @share
    def create__tremolite_2__match():
        alphanumeric_or_underscore = NAME('alphanumeric_or_underscore', ANY_OF('0-9', 'A-Z', '_', 'a-z'))
        letter_or_underscore       = NAME('letter_or_underscore',       ANY_OF('A-Z', '_', 'a-z'))
        ow                         = NAME('ow',                         ZERO_OR_MORE(' '))
        w                          = NAME('w',                          ONE_OR_MORE(' '))

        #
        #   Simple patterns
        #
        assign_operator     = NAME('assign_operator',     '=')
        colon               = NAME('colon',               ':')
        comma               = NAME('comma',               ',')
        comment_newline     = NAME('comment_newline',     P('#' + ZERO_OR_MORE(DOT)) + LINEFEED + END_OF_PATTERN)
        compare_equal       = NAME('compare_equal',       '==')
        dot                 = NAME('dot',                 '.')
        equal_sign          = NAME('equal_sign',          '=')
        greater_than_sign   = NAME('greater_than_sign',   '>')
        keyword_as          = NAME('as',                  'as')
        keyword_else        = NAME('else',                'else')
        keyword_except      = NAME('except',              'except')
        keyword_finally     = NAME('finally',             'finally')
        keyword_for         = NAME('for',                 'for')
        keyword_if          = NAME('if',                  'if')
        keyword_import      = NAME('import',              'import')
        keyword_in          = NAME('in',                  'in')
        keyword_is          = NAME('is',                  'is')
        keyword_not         = NAME('not',                 'not')
        keyword_or          = NAME('or',                  'or')
        keyword_print       = NAME('print',               'print')
        keyword_try         = NAME('try',                 'try')
        left_brace          = NAME('left_brace',          '{')                                #   }
        left_parenthesis    = NAME('left_parenthesis',    '(')                                #   )
        left_square_bracket = NAME('left_square_bracket', '[')                                #   ]
        less_than_sign      = NAME('less_than_sign',      '<')
        logical_and_sign    = NAME('logical_and_sign',    '&')
        logical_or_sign     = NAME('logical_or_sign',     '|')
        minus_sign          = NAME('minus_sign',          '-')
        not_equal           = NAME('not_equal',           '!=')
        percent_sign        = NAME('percent_sign',        '%')
        plus_sign           = NAME('plus_sign',           '+')
        semicolon           = NAME('semicolon',           ';')
        slash_sign          = NAME('slash_sign',          '/')
        star_sign           = NAME('star',                '*')
        tilde_sign          = NAME('tilde',               '~')

        name                = NAME('name',   letter_or_underscore + ZERO_OR_MORE(alphanumeric_or_underscore))
        number              = NAME('number', '0' | ANY_OF('1-9') + ZERO_OR_MORE(ANY_OF('0-9')))
        period              = NAME('period', '.')


        #   [(
        right_brace          = NAME('right_brace',             '}')
        right_parenthesis    = NAME('right_parenthesis',       ')')
        right_square_bracket = NAME('right_square_bracket',    ']')


        #
        #   More complicated patterns
        #
        ow_semicolon = NAME('ow_semicolon', ow + semicolon)


        #
        #   Generic
        #
        name_match = MATCH('name_match', name)

        #
        #   Line
        #
        MATCH(
            'line_match',
            (
                  ow
                + P(
                      G('keyword', keyword_import) + ow
                  )
                + Q(
                      'comment_newline',
                      P(
                            slash_sign
                          + slash_sign
                          + G('comment', ZERO_OR_MORE(ow + ONE_OR_MORE(NOT_ANY_OF('\x00-\x1F', ' '))))
                          + ow
                      )
                      + G('newline', LINEFEED + END_OF_PATTERN)
                  )
            ),
        )


        #
        #   Statements
        #
        MATCH(
            'import_pattern_match',
            ow + G('operator', period | 'import') + ow,
        )


        #
        #   Create ../Tremolite_2/Match.py
        #
        create_match_code('../Tremolite/Tremolite_2/Match.py', '2017-2018', 'Joy Diamond', 'Tremolite_2.Match')
