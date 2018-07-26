#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('TremoliteParser.Development')
def gem():
    show = 7


    @share
    def development():
        path = 'test.y'

        require_gem('TremoliteParser.Pattern')

        create__tremolite_parser__match()

        require_gem('TremoliteParser.Parse')                        #   Must be after `create__tremolite_parser__match`

        tree = parse_tremolite(path, test = 7, show = 0)

        if show is 7:
            for v in tree:
                dump_token('v', v)
