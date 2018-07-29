#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('Restructure.Core')
def module():
    require_module('Capital.Absent')                                       #   For built_in absent
    require_module('Capital.Import')                                       #   For built_in import_module
    require_module('Capital.PortrayString')                                #   For built_in portray_string


    transport('Capital.Ascii',                      'lookup_ascii')
    transport('Capital.Ascii',                      'unknown_ascii')
    transport('Capital.Cache',                      'produce_cache_functions')
    transport('Capital.DelayedFileOutput',          'create_DelayedFileOutput')
    transport('Capital.Path',                       'path_join')
    transport('Capital.Path',                       'read_text_from_path')
    transport('Capital.System',                     'module_path')
    transport('Capital.System',                     'python_version')
    transport('Rex.Compile',                        'compile_regular_expression')
    transport('Rex.Parse',                          'parse_ascii_regular_expression')
