#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('TremoliteParser.Development')
def module():
    show = 7


    @share
    def development():
        path = 'test.y'

        require_module('TremoliteParser.Pattern')

        create__tremolite_parser__match()

        require_module('TremoliteParser.Parse')                         #   Must be after `create__tremolite_parser__match`

        tree = parse_tremolite(path, test = 7, show = 0)

        if show is 7:
            for v in tree:
                dump_all_tokens('v', v)
