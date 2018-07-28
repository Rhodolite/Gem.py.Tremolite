#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('Restructure.Core')
def module():
    require_module('Capital.Absent')                                       #   For built_in absent
    require_module('Capital.Ascii')
    require_module('Capital.Cache')
    require_module('Capital.DelayedFileOutput')
    require_module('Capital.Exception')
    require_module('Capital.Import')                                       #   For built_in import_module
    require_module('Capital.Path')
    require_module('Capital.PortrayString')
    require_module('Capital.System')
    require_module('Rex.Compile')
    require_module('Rex.Parse')


    from Capital import create_DelayedFileOutput, lookup_ascii, module_path
    from Capital import path_join, produce_cache_functions, python_version, read_text_from_path, unknown_ascii
    from Rex import compile_regular_expression, parse_ascii_regular_expression


    share(
        #
        #   Imported functions (Capital)
        #
        'create_DelayedFileOutput',     create_DelayedFileOutput,
        'lookup_ascii',                 lookup_ascii,
        'path_join',                    path_join,
        'produce_cache_functions',      produce_cache_functions,
        'read_text_from_path',          read_text_from_path,


        #
        #   Imported functions (Rex)
        #
        'compile_regular_expression',       compile_regular_expression,
        'parse_ascii_regular_expression',   parse_ascii_regular_expression,


        #
        #   Values (Capital)
        #
        'module_path',          module_path,
        'python_version',       python_version,
        'unknown_ascii',        unknown_ascii,
    )
