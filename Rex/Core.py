#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('Rex.Core')
def gem():
    require_gem('Gem.Codec')
    require_gem('Gem.Map')


    from Gem import encode_ascii, first_map_item


    share(
        #
        #   Imported functions (Gem)
        #
        'encode_ascii',     encode_ascii,
        'first_map_item',   first_map_item,


        #
        #   Values
        #
        'list_of_single_none',  [none],
    )
