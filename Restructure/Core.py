#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('Restructure.Core')
def gem():
    require_gem('Gem.Absent')               #   For built_in absent
    require_gem('Gem.Ascii')
    require_gem('Gem.Cache')
    require_gem('Gem.DelayedFileOutput')
    require_gem('Gem.Exception')
    require_gem('Gem.Import')               #   For built_in import_module
    require_gem('Gem.Path')
    require_gem('Gem.PortrayString')
    require_gem('Gem.System')
    require_gem('Rex.Compile')
    require_gem('Rex.Parse')


    from Gem import create_DelayedFileOutput, lookup_ascii, module_path
    from Gem import path_join, produce_cache_functions, python_version, read_text_from_path, unknown_ascii
    from Rex import compile_regular_expression, parse_ascii_regular_expression


    share(
        #
        #   Imported functions (Gem)
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
        #   Values (Gem)
        #
        'module_path',          module_path,
        'python_version',       python_version,
        'unknown_ascii',        unknown_ascii,
    )
