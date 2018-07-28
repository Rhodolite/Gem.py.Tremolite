#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('TremoliteParser.Core')
def gem():
    require_gem('CoreParser.ActionWord')
    require_gem('CoreParser.ClassOrder')
    require_gem('CoreParser.CrystalComment')
    require_gem('CoreParser.CrystalIndentation')
    require_gem('CoreParser.BookcaseCoupleTwig')
    require_gem('CoreParser.DualFrill')
    require_gem('CoreParser.DualTwig')
    require_gem('CoreParser.DumpToken')
    require_gem('CoreParser.Elemental')
    require_gem('CoreParser.EmptyLine')
    require_gem('CoreParser.LineMarker')
    require_gem('CoreParser.Method')
    require_gem('CoreParser.Nub')
    require_gem('CoreParser.TestTree')
    require_gem('CoreParser.Tokenizer')
    require_gem('Gem.Cache')
    require_gem('Gem.Cache2')
    require_gem('Gem.DelayedFileOutput')
    require_gem('Gem.DumpCache')
    require_gem('Gem.Exception')
    require_gem('Gem.GeneratedConjureQuadruple')
    require_gem('Gem.Herd')
    require_gem('Gem.Method')
    require_gem('Gem.Path')
    require_gem('Gem.StringOutput')
    require_gem('Gem.System')
    require_gem('Gem.Traceback')


    from CoreParser import BookcaseCoupleTwig
    from CoreParser import CLASS_ORDER__NORMAL_TOKEN, conjure_any_comment_line, conjure_empty_line
    from CoreParser import conjure_indentation, conjure_keyword_language, conjure_line_marker, conjure_name
    from CoreParser import conjure_nub, conjure_vw_frill, construct__123
    from CoreParser import DualTwig, dump_token, KeywordAndOperatorBase
    from CoreParser import la, parse_context, ParserTrunk
    from CoreParser import produce_conjure_bookcase_couple_twig, produce_conjure_action_word
    from CoreParser import qd, qi, qj, qk, ql, qn, qs, raise_unknown_line, test_count_newlines, test_identical_output
    from CoreParser import wd, wd0, wd1, wi, wj, wk, wn, ws, z_initialize
    from Gem import create_cache, create_DelayedFileOutput, create_SimpleStringOutput, create_StringOutput
    from Gem import empty_herd, module_path, path_join, print_cache, print_exception_chain
    from Gem import produce_conjure_dual, produce_conjure_dual__21
    from Gem import produce_conjure_quadruple__4123
    from Gem import produce_conjure_single, produce_conjure_triple
    from Gem import produce_conjure_triple__312, produce_conjure_tuple
    from Gem import produce_conjure_unique_dual, produce_conjure_unique_dual__21
    from Gem import produce_conjure_unique_triple, produce_conjure_unique_triple__312
    from Gem import program_exit, read_text_from_path, return_self, slice_all, StringOutput


    share(
        #
        #   Types (CoreParser)
        #
        'BookcaseCoupleTwig',       BookcaseCoupleTwig,
        'DualTwig',                 DualTwig,
        'KeywordAndOperatorBase',   KeywordAndOperatorBase,
        'ParserTrunk',              ParserTrunk,


        #
        #   Types (Gem)
        #
        'StringOutput',     StringOutput,


        #
        #   Functions (CoreParser)
        #
        'conjure_any_comment_line',                 conjure_any_comment_line,
        'conjure_empty_line',                       conjure_empty_line,
        'conjure_indentation',                      conjure_indentation,
        'conjure_keyword_language',                 conjure_keyword_language,
        'conjure_line_marker',                      conjure_line_marker,
        'conjure_name',                             conjure_name,
        'conjure_nub',                              conjure_nub,
        'conjure_vw_frill',                         conjure_vw_frill,
        'construct__123',                           construct__123,
        'dump_token',                               dump_token,
        'la',                                       la,
        'produce_conjure_action_word',              produce_conjure_action_word,
        'produce_conjure_bookcase_couple_twig',     produce_conjure_bookcase_couple_twig,
        'qd',                                       qd,
        'qi',                                       qi,
        'qj',                                       qj,
        'qk',                                       qk,
        'ql',                                       ql,
        'qn',                                       qn,
        'qs',                                       qs,
        'raise_unknown_line',                       raise_unknown_line,
        'test_count_newlines',                      test_count_newlines,
        'test_identical_output',                    test_identical_output,
        'wd0',                                      wd0,
        'wd1',                                      wd1,
        'wd',                                       wd,
        'wi',                                       wi,
        'wj',                                       wj,
        'wk',                                       wk,
        'wn',                                       wn,
        'ws',                                       ws,
        'z_initialize',                             z_initialize,


        #
        #   Functions (Gem)
        #
        'create_cache',                         create_cache,
#       'create_DelayedFileOutput',             create_DelayedFileOutput,
#       'create_SimpleStringOutput',            create_SimpleStringOutput,
        'create_StringOutput',                  create_StringOutput,
        'path_join',                            path_join,
        'print_cache',                          print_cache,
        'print_exception_chain',                print_exception_chain,
#       'produce_conjure_dual__21',             produce_conjure_dual__21,
#       'produce_conjure_dual',                 produce_conjure_dual,
#       'produce_conjure_single',               produce_conjure_single,
#       'produce_conjure_triple__312',          produce_conjure_triple__312,
#       'produce_conjure_triple',               produce_conjure_triple,
#       'produce_conjure_tuple',                produce_conjure_tuple,
#       'produce_conjure_unique_dual__21',      produce_conjure_unique_dual__21,
        'produce_conjure_unique_dual',          produce_conjure_unique_dual,
#       'produce_conjure_quadruple__4123',      produce_conjure_quadruple__4123,
#       'produce_conjure_unique_triple',        produce_conjure_unique_triple,
        'produce_conjure_unique_triple__312',   produce_conjure_unique_triple__312,
        'program_exit',                         program_exit,
        'read_text_from_path',                  read_text_from_path,
#       'return_self',                          return_self,


        #
        #   Values (CoreParser)
        #
        'CLASS_ORDER__NORMAL_TOKEN',    CLASS_ORDER__NORMAL_TOKEN,
        'parse_context',                parse_context,


        #
        #   Values (Gem)
        #
        'module_path',          module_path,
    )
