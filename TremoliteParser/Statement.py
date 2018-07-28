#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('TremoliteParser.Statement')
def gem():
    require_gem('TremoliteParser.Core')


    class LanguagePattern(BookcaseCoupleTwig):
        display_name = 'language-pattern'
        is_herd      = false
        is_statement = true


    LanguagePattern.keyword_language = LanguagePattern.a
    LanguagePattern.keyword_pattern  = LanguagePattern.b

    
    conjure_language_pattern_statement = produce_conjure_bookcase_couple_twig(
            'language-pattern',
            LanguagePattern,
        )


    export(
        'conjure_language_pattern_statement',   conjure_language_pattern_statement,
    )
