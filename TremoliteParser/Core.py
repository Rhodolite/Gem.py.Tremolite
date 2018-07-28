#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('TremoliteParser.Core')
def module():
    require_module('Capital.Cache')
    require_module('Capital.Cache2')
    require_module('Capital.DelayedFileOutput')
    require_module('Capital.DumpCache')
    require_module('Capital.Exception')
    require_module('Capital.GeneratedConjureQuadruple')
    require_module('Capital.Herd')
    require_module('Capital.Method')
    require_module('Capital.Path')
    require_module('Capital.StringOutput')
    require_module('Capital.System')
    require_module('Capital.Traceback')
    require_module('CoreParser.ActionWord')
    require_module('CoreParser.BookcaseCoupleTwig')
    require_module('CoreParser.ClassOrder')
    require_module('CoreParser.CrystalComment')
    require_module('CoreParser.CrystalIndentation')
    require_module('CoreParser.DualFrill')
    require_module('CoreParser.DualTwig')
    require_module('CoreParser.DumpToken')
    require_module('CoreParser.Elemental')
    require_module('CoreParser.EmptyLine')
    require_module('CoreParser.LineMarker')
    require_module('CoreParser.Method')
    require_module('CoreParser.Nub')
    require_module('CoreParser.TestTree')
    require_module('CoreParser.Tokenizer')


    from Capital import create_cache, create_DelayedFileOutput, create_SimpleStringOutput, create_StringOutput
    from Capital import empty_herd, module_path, path_join, print_cache, print_exception_chain
    from Capital import produce_conjure_dual, produce_conjure_dual__21
    from Capital import produce_conjure_quadruple__4123
    from Capital import produce_conjure_single, produce_conjure_triple
    from Capital import produce_conjure_triple__312, produce_conjure_tuple
    from Capital import produce_conjure_unique_dual, produce_conjure_unique_dual__21
    from Capital import produce_conjure_unique_triple, produce_conjure_unique_triple__312
    from Capital import program_exit, read_text_from_path, return_self, slice_all, StringOutput
    from CoreParser import BookcaseCoupleTwig
    from CoreParser import CLASS_ORDER__NORMAL_TOKEN, conjure_any_comment_line, conjure_empty_line
    from CoreParser import conjure_indentation, conjure_keyword_language, conjure_line_marker, conjure_name
    from CoreParser import conjure_nub, conjure_vw_frill, construct__123
    from CoreParser import DualTwig, dump_token, KeywordAndOperatorBase
    from CoreParser import la, parse_context, ParserTrunk
    from CoreParser import produce_conjure_bookcase_couple_twig, produce_conjure_action_word
    from CoreParser import qd, qi, qj, qk, ql, qn, qs, raise_unknown_line, test_count_newlines, test_identical_output
    from CoreParser import wd, wd0, wd1, wi, wj, wk, wn, ws, z_initialize


    share(
        #
        #   Types (Capital)
        #
        'StringOutput',     StringOutput,


        #
        #   Types (CoreParser)
        #
        'BookcaseCoupleTwig',       BookcaseCoupleTwig,
        'DualTwig',                 DualTwig,
        'KeywordAndOperatorBase',   KeywordAndOperatorBase,
        'ParserTrunk',              ParserTrunk,


        #
        #   Functions (Capital)
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
        #   Values (Capital)
        #
        'module_path',          module_path,


        #
        #   Values (CoreParser)
        #
        'CLASS_ORDER__NORMAL_TOKEN',    CLASS_ORDER__NORMAL_TOKEN,
        'parse_context',                parse_context,
    )
