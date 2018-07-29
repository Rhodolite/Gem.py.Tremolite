#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('Rex.Core')
def module():
    transport('Capital.Codec',                      'encode_ascii')
    transport('Capital.Map',                        'first_map_item')


    share(
        #
        #   Values
        #
        'list_of_single_none',  [none],
    )
