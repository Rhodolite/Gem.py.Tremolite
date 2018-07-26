#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('TremoliteParser.Elemental')
def gem():
    @share
    class KeywordPattern(KeywordAndOperatorBase):
        __slots__    = (())
        class_order  = CLASS_ORDER__NORMAL_TOKEN
        display_name = 'pattern'
        keyword      = 'pattern'


    [
            conjure_keyword_pattern, conjure_keyword_pattern__ends_in_newline,
    ] = produce_conjure_action_word('keyword_pattern', KeywordPattern, produce_ends_in_newline = true)


    export(
        'conjure_keyword_pattern',                      conjure_keyword_pattern,
        'conjure_keyword_pattern__ends_in_newline',     conjure_keyword_pattern__ends_in_newline,
    )
