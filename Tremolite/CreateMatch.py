#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('Tremolite.CreateMatch')
def gem():
    require_gem('Tremolite.Name')


    @export
    def create_match_code(path, year, author, module_name):
        notice        = []
        append_notice = notice.append
        found         = 0
        debug         = false

        for v in iterate_values_sorted_by_key(match_cache):
            v.parse_ascii_regular_expression()

            debug |= v.debug


        for s in read_text_from_path('../Tremolite/OtherLicenses/LicenseTemplate.txt').splitlines():
            if s == '#':
                found = 1
            elif s == '<generated-output-goes-here />':
                found = 2

            if found is 1:
                append_notice(s)

        with create_DelayedFileOutput(path) as f:
            f.line('#')
            f.line('#   Copyright (c) %s %s.  All rights reserved.', year, author)
            f.line('#')
            f.line('@gem(%r)', module_name)

            with f.indent('def gem():'):
                f.line('require_gem(%r)', 'Gem.System')
                f.line('require_gem(%r)', 'Tremolite.Compile')

                if debug:
                    f.line('require_gem(%r)', 'Tremolite.PatternWrapper')

                f.blank2()
                f.line('from Gem import python_version')

                if debug:
                    f.line('from Tremolite import compile_regular_expression, create_wrapped_match_function')
                else:
                    f.line('from Tremolite import compile_regular_expression')

                f.blank2()

                with f.indent(arrange('if python_version == %s:', portray_string(python_version))):
                    with f.indent('C = ((', ')).__getitem__'):
                        for s in notice:
                            f.line(s)

                        f.line('0,')

                        for v in iterate_values_sorted_by_key(match_cache):
                            code   = v.code
                            groups = v.groups
                            flags  = v.flags

                            f.blank()
                            f.line('#')
                            f.line('#   %s', portray_string(v.pattern.regular_expression))
                            f.line('#')

                            if type(code) is String:
                                f.line('%s,', portray_string(code))
                            else:
                                with f.indent('((', ')),'):
                                    data     = none
                                    position = 0

                                    for w in code:
                                        if (is_python_2) and (type(w) is Long):
                                            s = arrange('Long(%d)', w)
                                        else:
                                            s = arrange('%d', w)

                                        s_total = length(s)

                                        if (position is not 0) and (position + s_total + 2) > 120:
                                            f.line(data)
                                            position = 0

                                        if position is 0:
                                            data     = s + ','
                                            position = f.prefix_total + s_total + 1
                                        else:
                                            data     += ' ' + s + ','
                                            position += 1 + s_total + 1

                                    f.line(data)

                            if groups is not 0:
                                f.line('((%s)),',
                                       ', '.join(('none'   if v is none else   portray_string(v))   for v in groups))

                            if flags is not 0:
                                f.line('%d,', flags)

                        f.line('#</copyright>')


                    if debug:
                        f.blank2()

                        with f.indent('def D(name, regular_expression, code, groups = 0, flags = 0):'):
                            with f.indent('return create_wrapped_match_function(', '       )', 11):
                                f.line('intern_string(name),')
                                f.line('regular_expression,')
                                f.line('C(code),')
                                f.line('C(groups),')
                                f.line('C(flags),')

                    f.blank2()

                    with f.indent('def M(regular_expression, code, groups = 0, flags = 0):'):
                        f.line('return compile_regular_expression(regular_expression, C(code), C(groups), C(flags)).match')

                f.blank2()

                with f.indent('else:'):
                    f.line('require_gem(%r)', 'Tremolite.Parse')
                    f.blank2()
                    f.line('from Tremolite import parse_ascii_regular_expression')

                    if debug:
                        f.blank2()

                        with f.indent('def D(name, regular_expression, code, groups = 0, flags = 0):'):
                            with f.indent('return create_wrapped_match_function(', '       )', 11):
                                f.line('intern_string(name),')
                                f.line('regular_expression,')
                                f.line('*parse_ascii_regular_expression(regular_expression)#,')

                    f.blank2()

                    with f.indent('def M(regular_expression, code, groups = 0, flags = 0):'):
                        with f.indent('return compile_regular_expression(', ').match'):
                            f.line('regular_expression,')
                            f.line('*parse_ascii_regular_expression(regular_expression)#,')

                if name_cache:
                    f.blank2()

                    for v in iterate_values_sorted_by_key(name_cache):
                        f.line('#')
                        f.line('#   %s = %s', v.name, v.pattern)

                    f.line('#')

                f.blank2()

                index = 1

                for v in iterate_values_sorted_by_key(match_cache):
                    code   = v.code
                    groups = v.groups
                    flags  = v.flags

                    f.blank()
                    f.line('#')
                    f.line('#   %s', v.name)
                    f.line('#')
                    f.line('#       %s', v.pattern)
                    f.line('#')

                    with f.indent(
                            arrange('%s = %s(', v.name, ('D'    if v.debug else    'M')),
                            ')',
                    ):
                        if v.debug:
                            f.line('%s,', portray_string(v.name))

                        f.line('%s,', portray_string(v.pattern.regular_expression))
                        f.line('%d,', index)
                        index += 1

                        if groups is not 0:
                            f.line('%d,', index)
                            index += 1
                        elif flags is not 0:
                            f.line('0,')

                        if flags is not 0:
                            f.line('%d,', index)
                            index += 1

                f.blank2()

                total = maximum(length(v.name)   for v in iterate_values_sorted_by_key(match_cache))
                total = (total + 8) &~ 3

                with f.indent(
                    'export(',
                    ')',
                ):
                    for v in iterate_values_sorted_by_key(match_cache):
                        f.line('%*s%s,', -total, arrange('%r,', v.name), v.name)

            data = f.finish()
