#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('TremoliteParser.Core')
def gem():
    require_gem('CoreParser.Elemental')
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


    from CoreParser import conjure_keyword_import, conjure_keyword_import__ends_in_newline, conjure_name
    from CoreParser import la, parse_context, qd, qi, qj, qk, ql, qn, qs, raise_unknown_line
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
        #   Imported types
        #
        'StringOutput',     StringOutput,


        #
        #   Imported functions (CoreParser)
        #
        'conjure_keyword_import',                   conjure_keyword_import,
        'conjure_keyword_import__ends_in_newline',  conjure_keyword_import__ends_in_newline,
        'conjure_name',                             conjure_name,
        'la',                                       la,
        'qd',                                       qd,
        'qi',                                       qi,
        'qj',                                       qj,
        'qk',                                       qk,
        'ql',                                       ql,
        'qn',                                       qn,
        'qs',                                       qs,
        'raise_unknown_line',                       raise_unknown_line,
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
        #   Imported functions (Gem)
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
#       'produce_conjure_unique_dual',          produce_conjure_unique_dual,
#       'produce_conjure_quadruple__4123',      produce_conjure_quadruple__4123,
#       'produce_conjure_unique_triple',        produce_conjure_unique_triple,
#       'produce_conjure_unique_triple__312',   produce_conjure_unique_triple__312,
        'program_exit',                         program_exit,
        'read_text_from_path',                  read_text_from_path,
#       'return_self',                          return_self,


        #
        #   Values (CoreParser)
        #
        'parse_context',                            parse_context,


        #
        #   Values (Gem)
        #
#       'empty_herd',           empty_herd,
        'module_path',          module_path,
#       'slice_all',            slice_all,
#       'tuple_of_2_nones',     ((none, none)),
    )
