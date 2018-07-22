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
    module_path.insert(2, path_absolute(path_join(path_0, '../../Parser')))


    import Gem


@gem('TremoliteParser.Main')
def gem():
    require_gem('TremoliteParser.Core')


    show  = 0


    def command_parse1(
            remove_comments    = false,
            remove_indentation = false,
            show               = 0,
    ):
        require_gem('TremoliteParser.Pattern')

        create__tremolite_parser__match()

        require_gem('TremoliteParser.Parse')                            #   Must be after `create__tremolite_parser__match`

        parse_java('test.java', test = 7, show = show)

        #for name in ['arguments-2', 'list-expression-2', 'range-index', 'tuple-expression-2']:
        #    print_cache(name)

        print_cache()


    @share
    def main(arguments):
        try:
            total = length(arguments)

            if total is 0:
                return command_parse1()

            if total is not 1:
                raise_runtime_error('must have zero or one argument')

            option = arguments[0]

            if option == 'dev':
                return command_parse1()

            raise_runtime_error('unknown option: %r', option)
        except:
            with except_any_clause() as e:
                print_exception_chain(e)
                program_exit(1)
