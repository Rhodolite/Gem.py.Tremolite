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
    module_path.insert(1, path_absolute(path_join(path_0, '../../Capital')))
    module_path.insert(2, path_absolute(path_join(path_0, '../../Parser')))


    import Capital


@module('TremoliteParser.Main')
def module():
    transport('Capital.Global',                     'capital_global')


    capital_global.crystal_parser   = true
    capital_global.tremolite_parser = true


    require_module('TremoliteParser.Core')


    show = 0


    def command_development():
        require_module('TremoliteParser.Development')

        development()


    @share
    def main(arguments):
        try:
            total = length(arguments)

            if total is 0:
                return command_development()

            if total is not 1:
                raise_runtime_error('must have zero or one argument')

            option = arguments[0]

            if option == 'dev':
                return command_development()

            raise_runtime_error('unknown option: %r', option)
        except:
            with except_any_clause() as e:
                print_exception_chain(e)
                program_exit(1)
