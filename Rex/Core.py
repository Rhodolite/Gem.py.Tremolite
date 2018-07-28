#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('Rex.Core')
def module():
    require_module('Capital.Codec')
    require_module('Capital.Map')


    from Capital import encode_ascii, first_map_item


    share(
        #
        #   Imported functions (Capital)
        #
        'encode_ascii',     encode_ascii,
        'first_map_item',   first_map_item,


        #
        #   Values
        #
        'list_of_single_none',  [none],
    )
