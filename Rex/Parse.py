#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('Rex.Parse')
def module():
    require_module('Rex.Core')


    PythonRegularExpressionCompile = import_module('sre_compile')
    PythonRegularExpressionParse   = import_module('sre_parse')


    @export
    def parse_ascii_regular_expression(regular_expression, flags = 0):
        assert type(regular_expression) is String
        assert type(flags)              is Integer


        #
        #<copyright>
        #   Some of this code is from the python standard library 'sre_compile.py', function 'compile' & is thus:
        #
        #       Copyright (c) 1998-2001 by Secret Labs AB.  All rights reserved.
        #
        #       This version of the SRE library can be redistributed under CNRI's
        #       Python 1.6 license.  For any other use, please contact Secret Labs
        #       AB (info@pythonware.com).
        #
        #   (Currently the same copyright is used for both python 2.7 & 3.5 versions)
        #
        #   P.S.:  To make things simple, all *changes* to the original code below are dual licensed under
        #          both (1) the MIT License that the rest of Gem is licensed; and (2) under the exact same
        #          "CNRI's Python 1.6" license as the original code.
        #
        #   NOTE:  Dual copyright only applies to the changes, not to the original code which is obviously
        #          only licensed under the original license.
        #
        python__create_regular_expression_code = PythonRegularExpressionCompile._code
        python__parse_regular_expression       = PythonRegularExpressionParse.parse

        p    = python__parse_regular_expression(encode_ascii(regular_expression), flags)
        code = python__create_regular_expression_code(p, flags)

        for i in code:
            if not (0 <= i <= 255):
                code = Tuple(code)
                break
        else:
            code = ''.join(character(i)   for i in code)

        p_pattern  = p.pattern
        full_flags = flags | p_pattern.flags
        groups     = p_pattern.groups
        group_map  = p_pattern.groupdict

        if groups is 1:
            assert length(group_map) is 0

            return ((code, 0, full_flags))

        if groups is 2:
            assert length(group_map) is 1

            [k, i] = first_map_item(group_map)

            assert i is 1

            return ((code, (( none, intern_string(k) )), full_flags))

        if is_python_2:
            if groups > 100:
                raise_value_error('More than 100 groups not implemented in python 2')

        assert groups == 1 + length(group_map)

        index_group = list_of_single_none * groups

        for [k, i] in view_items(group_map):
            assert index_group[i] is none

            index_group[i] = intern_string(k)

        return ((code, Tuple(index_group), full_flags))
    #</copyright>
