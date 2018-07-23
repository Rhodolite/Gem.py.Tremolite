#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('TremoliteParser.Tree')
def gem():
    @share
    class TremoliteParserTrunk(Object):
        __slots__ = (())


        is_comment_line            = false              #   Not yet used
        is_comment__or__empty_line = false              #   Not yet used
        is_empty_line              = false              #   Not yet used
        is_end_of_data             = false              #   Not yet used
        is_statement               = false              #   Not yet used


        if 0:                                                           #   Not currently used
            def display_full_token(t):
                return t.display_token()


        #nub = static_conjure_nub
