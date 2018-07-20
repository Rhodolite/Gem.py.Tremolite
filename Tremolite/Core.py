#
#   Copyright (c) 2017 Joy Diamond.  All rights reserved.
#
@gem('Tremolite.Core')
def gem():
    require_gem('Gem.Absent')               #   For built_in absent
    require_gem('Gem.Ascii')
    require_gem('Gem.Cache')
    require_gem('Gem.Codec')
    require_gem('Gem.DelayedFileOutput')
    require_gem('Gem.Exception')
    require_gem('Gem.Import')               #   For built_in import_module
    require_gem('Gem.Map')
    require_gem('Gem.Path')
    require_gem('Gem.PortrayString')
    require_gem('Gem.System')


    from Gem import create_DelayedFileOutput, encode_ascii, first_map_item, lookup_ascii
    from Gem import produce_cache_functions, python_version, read_text_from_path, unknown_ascii


    share(
        #
        #   Imported functions
        #
        'create_DelayedFileOutput',     create_DelayedFileOutput,
        'encode_ascii',                 encode_ascii,
        'first_map_item',               first_map_item,
        'lookup_ascii',                 lookup_ascii,
        'produce_cache_functions',      produce_cache_functions,
        'read_text_from_path',          read_text_from_path,


        #
        #   Values
        #
        'list_of_single_none',  [none],
        'python_version',       python_version,
        'unknown_ascii',        unknown_ascii,
    )
