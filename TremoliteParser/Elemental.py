#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('TremoliteParser.Elemental')
def module():
    @share
    class KeywordPattern(KeywordAndOperatorBase):
        __slots__    = (())
        class_order  = CLASS_ORDER__NORMAL_TOKEN
        display_name = 'pattern'
        keyword      = 'pattern'


    class OperatorColonEqual(KeywordAndOperatorBase):
        __slots__    = (())
        class_order  = CLASS_ORDER__NORMAL_TOKEN
        display_name = ':'
        keyword      = ':'


    conjure_colon_equal     = produce_conjure_action_word('colon_equal',     OperatorColonEqual)
    conjure_keyword_pattern = produce_conjure_action_word('keyword_pattern', KeywordPattern)


    W__COLON_EQUAL__W = conjure_colon_equal(' := ')


    find_atom_type = {
            '"' : conjure_double_quote,
            "'" : conjure_single_quote,
        }.__getitem__


    export(
        'conjure_colon_equal',      conjure_colon_equal,
        'W__COLON_EQUAL__W',        W__COLON_EQUAL__W,
        'conjure_keyword_pattern',  conjure_keyword_pattern,
        'find_atom_type',           find_atom_type,
    )
