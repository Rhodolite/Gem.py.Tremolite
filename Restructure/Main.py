#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
def boot(module_name):
    def execute(f):
        return f()

    return execute


@boot('Boot')
def boot():
    from sys     import path    as module_path
    from os.path import abspath as path_absolute, join as path_join

    path_0 = module_path[0]

    module_path.insert(0, path_absolute(path_join(path_0, '../')))
    module_path.insert(1, path_absolute(path_join(path_0, '../../Gem')))


    import Gem


@gem('Restructure.Main')
def gem():
    require_gem('Restructure.Core')
    require_gem('Restructure.Name')
    require_gem('Restructure.Build')
    require_gem('Restructure.CreateMatch')


    @share
    def main(arguments):
        identifier = NAME('identifier', ANY_OF('A-Z', '_', 'a-z') + ZERO_OR_MORE(ANY_OF('0-9', 'A-Z', '_', 'a-z')))

        #MATCH('test', PRINTABLE_MINUS("'", '\\'))

        FULL_MATCH('name_match', identifier)
        create_match_code(
                path_join(module_path[0], 'Restructure/Match.py'),
                '2017-2018',
                'Joy Diamond',
                'Restructure.Match',
            )
