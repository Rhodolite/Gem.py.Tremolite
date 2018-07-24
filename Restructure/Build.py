#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('Restructure.Build')
def gem():
    require_gem('Restructure.Core')
    require_gem('Restructure.Match')


    show = false


    #
    #   RestructureBase
    #       RestructureExact
    #       RestructureGroupBase
    #           RestructureGroup
    #           RestructureName
    #           RestructureNamedGroup
    #           RestructureOptionalGroup
    #       RestructureMany
    #           RestructureAdd
    #           RestructureAnyOf
    #           RestructureOr
    #       RestructureOne
    #           RestructureNotFollowedBy
    #           RestructureOptional
    #           RestructureParenthesis
    #           RestructureRepeat
    #       RestructureSpecial
    #
    class RestructureBase(Object):
        __slots__ = ((
            'regular_expression',       #   String
            'portray',                  #   String
        ))


        is_restructure_or = false


        #def __init__(t, regular_expression, portray):
        #    t.regular_expression = regular_expression
        #    t.portray            = portray


        def __add__(t, that):
            if type(that) is String:
                that = INVISIBLE_EXACT(that)
            elif that.is_restructure_or:
                that = wrap_parenthesis(that)

            return RestructureAdd(
                       t.regular_expression + that.regular_expression,
                       t.portray + ' + ' + that.portray,
                       ((t, that)),
                   )


        def __or__(t, that):
            if type(that) is String:
                that = INVISIBLE_EXACT(that)
            else:
                assert not that.is_restructure_or

            return RestructureOr(
                       t.regular_expression + '|' + that.regular_expression,
                       t.portray + ' | ' + that.portray,
                       ((t, that)),
                   )


        def __radd__(t, that):
            return INVISIBLE_EXACT(that) + t


        def __ror__(t, that):
            return INVISIBLE_EXACT(that) | t


        def __str__(t):
            return t.portray


        def compile_ascii_regular_expression(t):
            return compile_regular_expression(
                       t.regular_expression,
                       *parse_ascii_regular_expression(t.regular_expression)
                   )


    class RestructureExact(RestructureBase):
        __slots__ = ((
            'exact',                    #   String
            'singular',                 #   Boolean
        ))


        is_restructure_exact = true
        optional             = true
        repeatable           = true


        def __init__(t, regular_expression, portray, exact, singular):
            t.regular_expression = regular_expression
            t.portray            = portray
            t.exact              = exact
            t.singular           = singular


        def __repr__(t):
            suffix = ('; singular'    if t.singular else    '')

            if t.regular_expression is t.exact:
                return arrange('<RestructureExact %s%s>', portray_string(t.regular_expression), suffix)

            return arrange('<RestructureExact %s %s%s>',
                           portray_string(t.regular_expression),
                           portray_string(t.exact),
                           suffix)


    class RestructureGroupBase(RestructureBase):
        __slots__ = ((
            'name',                     #   String
            'pattern',                  #   String
        ))


        def __init__(t, regular_expression, portray, name, pattern):
            t.regular_expression = regular_expression
            t.portray            = portray
            t.name               = name
            t.pattern            = pattern


        def __repr__(t):
            return arrange('<%s %s %r>', t.__class__.__name__, t.name, t.pattern)


        @property
        def optional(t):
            return t.pattern.optional


        @property
        def repeatable(t):
            return t.pattern.repeatable


        @property
        def singular(t):
            return t.pattern.singular


    class RestructureGroup(RestructureGroupBase):
        __slots__ = (())


    class RestructureName(RestructureGroupBase):
        __slots__ = (())


        is_restructure_name = true


        def __init__(t, name, pattern):
            t.regular_expression = pattern.regular_expression
            t.portray            = t.name = name
            t.pattern            = pattern


    class RestructureNamedGroup(RestructureGroupBase):
        __slots__ = (())


    class RestructureOptionalGroup(RestructureGroupBase):
        __slots__ = (())


        optional   = false
        repeatable = false
        singular   = false


    class RestructureMany(RestructureBase):
        __slots__ = ((
            'many',                     #   Tuple of RestructureBase+
        ))


        optional   = true
        repeatable = true


        def __init__(t, regular_expression, portray, many):
            t.regular_expression = regular_expression
            t.portray            = portray
            t.many               = many


        def __repr__(t):
            return arrange('<%s %s %s>',
                           t.__class__.__name__,
                           portray_string(t.regular_expression),
                           ' '.join((portray_string(v)   if type(v) is String else   portray(v))   for v in t.many))


    class RestructureAdd(RestructureMany):
        __slots__ = (())


        singular = false


        def __add__(t, that):
            if type(that) is String:
                that = INVISIBLE_EXACT(that)
            elif that.is_restructure_or:
                that = wrap_parenthesis(that)

            return RestructureAdd(
                       t.regular_expression + that.regular_expression,
                       t.portray + ' + ' + that.portray,
                       t.many + ((that,)),
                   )


    class RestructureAnyOf(RestructureMany):
        __slots__ = (())


        singular = true


        def __repr__(t):
            return arrange('<RestructureAnyOf %s %s>',
                           portray_string(t.regular_expression),
                           ' '.join(portray_string(v)   for v in t.many))


    class RestructureOr(RestructureMany):
        __slots__ = (())


        is_restructure_or = true
        singular          = false


        def __add__(t, that):
            return wrap_parenthesis(t) + that


        def __or__(t, that):
            if type(that) is String:
                that = INVISIBLE_EXACT(that)

            return RestructureOr(
                       t.regular_expression + '|' + that.regular_expression,
                       t.portray + ' | ' + that.portray,
                       t.many + ((that,)),
                   )


    class RestructureOne(RestructureBase):
        __slots__ = ((
            'pattern',                  #   String
        ))


        singular = true


        def __init__(t, regular_expression, portray, pattern):
            t.regular_expression = regular_expression
            t.portray            = portray
            t.pattern            = pattern


        def __repr__(t):
            return arrange('<%s %s %r>', t.__class__.__name__, portray_string(t.regular_expression), t.pattern)


    class RestructureNotFollowedBy(RestructureOne):
        __slots__ = (())


        optional   = false
        repeatable = false


    class RestructureOptional(RestructureOne):
        __slots__ = (())


        optional   = false
        repeatable = false


    class RestructureParenthesis(RestructureOne):
        __slots__ = (())


        optional   = true
        repeatable = true


        def __init__(t, regular_expression, portray, pattern):
            assert pattern.optional
            assert pattern.repeatable

            t.regular_expression = regular_expression
            t.portray            = portray
            t.pattern            = pattern


    class RestructureRepeat(RestructureOne):
        __slots__ = (())


        optional   = true
        repeatable = false
        singular   = true


    class RestructureSpecial(RestructureBase):
        __slots__ = ((
            'repeatable',               #   Boolean
            'singular',                 #   Boolean
        ))


        def __init__(t, regular_expression, portray, repeatable, singular):
            t.regular_expression = intern_string(regular_expression)
            t.portray            = intern_string(portray)
            t.repeatable         = repeatable
            t.singular           = singular


        def __repr__(t):
            if t.repeatable:
                if t.singular:
                    suffix = '; repeatable & singular'
                else:
                    suffix = '; repeatable'
            else:
                if t.singular:
                    suffix = '; singular'                   #   Can't happen -- here for completeness
                else:
                    suffix = ''

            return arrange('<RestructureSpecial %s %s%s>', portray_string(t.regular_expression), t.portray, suffix)


    RestructureSpecial.optional = RestructureSpecial.repeatable


    [
            name_cache, name_insert_interned,
    ] = produce_cache_functions(
            'name', RestructureName,

            produce_cache           = true,
            produce_insert_interned = true,
        )


    def create_any_of(name, begin, end, arguments):
        assert length(arguments) > 0

        regular_expressions = [begin]
        portray             = []
        many                = []

        for v in arguments:
            if v is LINEFEED:
                regular_expressions.append(r'\n')
                portray.append(v.portray)
                many.append(v)
                continue

            if type(v) is not String:
                assert (v.is_restructure_name) and (v.pattern.is_restructure_exact) and (v.pattern.singular)

                v = v.pattern.exact

                assert length(v) is 1

                if v == '-':
                    regular_expressions.append(r'\-')
                else:
                    a = lookup_ascii(v)

                    assert a.is_printable

                    regular_expressions.append(a.pattern)

            elif length(v) is 1:
                if v == '-':
                    regular_expressions.append(r'\-')
                else:
                    a = lookup_ascii(v)

                    assert a.is_printable

                    regular_expressions.append(a.pattern)
            else:
                assert (length(v) is 3) and (v[1] is '-')

                a0 = lookup_ascii(v[0])
                a2 = lookup_ascii(v[2])

                if (not a0.is_printable) and (a0.ordinal >= 32):
                    raise_runtime_error('invalid character <%s> passed to %s(%s)',
                                            portray_string(v[0]), name, portray_string(v))

                if (not a2.is_printable) and (a2.ordinal >= 32):
                    raise_runtime_error('invalid character <%s> passed to %s(%s)',
                                        portray_string(v[2]), name, portray_string(v))

                regular_expressions.append(a0.pattern + '-' + a2.pattern)

            portray.append(portray_string(v))
            many.append(intern_string(v))

        regular_expressions.append(end)

        return RestructureAnyOf(
                   intern_string(''.join(regular_expressions)),
                   intern_arrange('%s(%s)', name, ', '.join(portray)),
                   Tuple(many),
               )


    def create_exact(s):
        assert length(s) >= 1

        many   = []
        append = many.append

        for c in s:
            a = lookup_ascii(c)

            if not a.is_printable:
                raise_runtime_error('invalid character <%s> passed to EXACT(%s)', portray_string(c), portray_string(s))

            append(a.pattern)

        return intern_string(''.join(many))


    def create_repeat(name, pattern, m, n, question_mark = false):
        if type(pattern) is String:
            pattern = INVISIBLE_EXACT(pattern)
        else:
            assert pattern.repeatable

        prefix = (pattern.regular_expression   if pattern.singular else   '(?:' + pattern.regular_expression + ')')

        if n is none:
            assert m >= 2

            if question_mark:
                return RestructureOptional(
                           intern_arrange('%s{%d}?', suffix, m),
                           arrange('%s(%s, %d)', name, pattern, m),
                           pattern,
                       )

            return RestructureRepeat(
                       intern_arrange('%s{%d}', suffix, m),
                       arrange('%s(%s, %d)', name, pattern, m),
                       pattern,
                   )

        if n == -7:
            assert m >= 0

            if m is 0:
                suffix = '{,}'
            else:
                suffix = arrange('{%d,}', m)

            if question_mark:
                return RestructureOptional(
                           intern_string(prefix + suffix + '?'),
                           arrange('%s(%s, %d)', name, pattern, m),
                           pattern,
                       )

            return RestructureRepeat(
                       intern_string(prefix + suffix),
                       arrange('%s(%s, %d)', name, pattern, m),
                       pattern,
                   )

        assert 0 <= m < n

        if m is 0:
            suffix = arrange('{,%d}', n)
        else:
            suffix = arrange('{%d,%d}', m, n)

        if question_mark:
            return RestructureOptional(
                       intern_string(prefix + suffix + '?'),
                       arrange('%s(%s, %d, %d)', name, pattern, m, n),
                       pattern,
                   )

        return RestructureRepeat(
                   intern_string(prefix + suffix),
                   arrange('%s(%s, %d, %d)', name, pattern, m, n),
                   pattern,
               )


    def create_simple_repeat(name, pattern, suffix, question_mark = false):
        if type(pattern) is String:
            pattern = INVISIBLE_EXACT(pattern)
        else:
            assert pattern.repeatable

        if question_mark:
            return RestructureOptional(
                       (
                           intern_string(pattern.regular_expression + suffix + '?')
                               if pattern.singular else
                                   intern_arrange('(?:%s)%s?', pattern.regular_expression, suffix)
                       ),
                       arrange('%s(%s)', name, pattern),
                       pattern,
                   )

        return RestructureRepeat(
                   (
                       intern_string(pattern.regular_expression + suffix)
                           if pattern.singular else
                               intern_arrange('(?:%s)%s', pattern.regular_expression, suffix)
                   ),
                   arrange('%s(%s)', name, pattern),
                   pattern,
               )


    def wrap_parenthesis(pattern, invisible = false):
        assert not pattern.singular

        return RestructureParenthesis(
                   intern_arrange('(?:%s)', pattern.regular_expression),
                   (pattern.portray   if invisible else   intern_arrange('(%s)', pattern.portray)),
                   pattern,
               )


    @export
    def ANY_OF(*arguments):
        return create_any_of('ANY_OF', '[', ']', arguments)


    @export
    def EXACT(s):
        assert length(s) >= 1

        return RestructureExact(
                   create_exact(s), intern_arrange('EXACT(%s)', portray_string(s)), intern_string(s), length(s) is 1,
               )


    @export
    def G(name, pattern = absent):
        if pattern is absent:
            assert name.is_restructure_name

            return RestructureGroup(
                       intern_arrange('(?P<%s>%s)', name.name, name.regular_expression),
                       arrange('G(%s)', portray_string(name.name)),
                       name,
                       name,
                   )

        if name_match(name) is none:
            raise_runtime_error('G: invalid group name: %s (expected a python identifier)', name)

        if type(pattern) is String:
            pattern = INVISIBLE_EXACT(pattern)

        return RestructureGroup(
                   intern_arrange('(?P<%s>%s)', name, pattern.regular_expression),
                   arrange('G(%s, %s)', portray_string(name), pattern),
                   name,
                   pattern,
               )


    @export
    def INVISIBLE_EXACT(s):
        assert (type(s) is String) and (length(s) >= 1)

        return RestructureExact(
                   create_exact(s), intern_string(portray_string(s)), intern_string(s), length(s) is 1,
               )


    @export
    def MINIMUM_OF_ONE_OR_MORE(pattern):
        return create_simple_repeat('MINIMUM_OF_ONE_OR_MORE', pattern, '{1,7777777}', question_mark = true)


    @export
    def MINIMUM_OF_OPTIONAL(pattern):
        return create_simple_repeat('MINIMUM_OF_OPTIONAL', pattern, '?', question_mark = true)


    @export
    def MINIMUM_OF_REPEAT(pattern, m, n = none):
        return create_repeat('MINIMUM_OF_REPEAT', pattern, m, n, question_mark = true)


    @export
    def MINIMUM_OF_REPEAT_OR_MORE(pattern, m):
        return create_repeat('MINIMUM_OF_REPEAT_OR_MORE', pattern, m, 7777777, question_mark = true)


    @export
    def MINIMUM_OF_ZERO_OR_MORE(pattern):
        return create_simple_repeat('MINIMUM_OF_ZERO_OR_MORE', pattern, '{,7777777}', question_mark = true)


    @export
    def NAME(name, pattern):
        if name_match(name) is none:
            raise_runtime_error('NAME: invalid name: %s (expected a python identifier)', name)

        if type(pattern) is String:
            pattern = INVISIBLE_EXACT(pattern)

        interned_name = intern_string(name)

        return name_insert_interned(interned_name, RestructureName(interned_name, pattern))


    @export
    def NAMED_GROUP(name, pattern):
        if name_match(name) is none:
            raise_runtime_error('NAMED_GROUP: invalid name: %s (expected a python identifier)', name)

        if type(pattern) is String:
            pattern = INVISIBLE_EXACT(pattern)

        interned_name = intern_string(name)

        return name_insert_interned(
                   interned_name,
                   RestructureNamedGroup(
                       intern_arrange('(?P<%s>%s)', interned_name, pattern.regular_expression),
                       interned_name,
                       interned_name,
                       G(interned_name, pattern),
                   ),
               )


    @export
    def NOT_ANY_OF(*arguments):
        return create_any_of('NOT_ANY_OF', '[^', ']', arguments)


    @export
    def NOT_FOLLOWED_BY(pattern):
        if type(pattern) is String:
            pattern = INVISIBLE_EXACT(pattern)

        return RestructureNotFollowedBy(
                   intern_arrange('(?!%s)', pattern.regular_expression),
                   intern_arrange('NOT_FOLLOWED_BY(%s)', pattern.portray),
                   pattern,
               )


    @export
    def ONE_OR_MORE(pattern):
        return create_simple_repeat('ONE_OR_MORE', pattern, '{1,7777777}')


    @export
    def OPTIONAL(pattern):
        return create_simple_repeat('OPTIONAL', pattern, '', question_mark = true)


    @export
    def Q(name, pattern = absent):
        if pattern is absent:
            assert name.is_restructure_name

            return RestructureGroup(
                       intern_arrange('(?P<%s>%s)?', name.name, name.regular_expression),
                       arrange('Q(%s)', portray_string(name.name)),
                       name,
                       name,
                   )

        if type(pattern) is String:
            pattern = INVISIBLE_EXACT(pattern)
        else:
            assert pattern.optional

        if name_match(name) is none:
            raise_runtime_error('Q: invalid group name: %s (expected a python identifier)', name)

        return RestructureOptionalGroup(
                   intern_arrange('(?P<%s>%s)?', name, pattern.regular_expression),
                   arrange('Q(%s, %s)', portray_string(name), pattern),
                   name,
                   pattern,
               )


    #
    #<PRINTABLE_MINUS>
    #
    def raise_invalid_printable_minus_character(c, s):
        raise_runtime_error('invalid character <%s> passed to PRINTABLE_MINUS(%s)',
                            portray_string(c), portray_string(s))


    def raise_already_not_allowed_printable_minus_character(c, s):
        raise_runtime_error('character %r already not allowed in PRINTABLE_MINUS(%s)',
                            portray_string(c), portray_string(s))


    ordinal_space = ordinal(' ')
    ordinal_minus = ordinal('-')
    ordinal_tilde = ordinal('~')


    @export
    def PRINTABLE_MINUS(*arguments):
        assert length(arguments) > 0

        valid = [ordinal_space <= i <= ordinal_tilde   for i in iterate_range(0, 256)]

        for v in arguments:
            if type(v) is not String:
                assert (v.is_restructure_name) and (v.pattern.is_restructure_exact) and (v.pattern.singular)

                v = v.pattern.exact

                assert length(v) is 1

                a = lookup_ascii(v, unknown_ascii)

                if not a.is_printable:
                    raise_invalid_printable_minus_character(v, v)

                if not valid[a.ordinal]:
                    raise_already_not_allowed_printable_minus_character(v, v)

                valid[a.ordinal] = false
                continue

            if length(v) is 1:
                a = lookup_ascii(v, unknown_ascii)

                if not a.is_printable:
                    raise_invalid_printable_minus_character(v, v)

                if not valid[a.ordinal]:
                    raise_already_not_allowed_printable_minus_character(v, v)

                valid[a.ordinal] = false
                continue

            assert (length(v) is 3) and (v[1] is '-')

            a0 = lookup_ascii(v[0], unknown_ascii)
            a2 = lookup_ascii(v[2], unknown_ascii)

            if not a0.is_printable:
                raise_invalid_printable_minus_character(v[0], v)

            if not a2.is_printable:
                raise_invalid_printable_minus_character(v[2], v)

            if a0.ordinal > a2.ordinal:
                raise_runtime_error('invalid backwards range PRINTABLE_MINUS(%s)', portray_string(v))

            for i in iterate_range(a0.ordinal, a2.ordinal):
                if not valid[i]:
                    raise_already_not_allowed_printable_minus_character(character(i), v)

                valid[i] = false

        regular_expressions       = ['[']
        append_regular_expression = regular_expressions.append
        lowest                    = none

        def add_range(lowest, highest):
            if show:
                line('add_range(%d, %d)', lowest, highest)

            if lowest == ordinal_minus:
                regular_expressions.insert(0, '-')
                lowest += 1

            if highest == ordinal_minus:
                regular_expressions.insert(0, '-')
                highest -= 1

            if lowest == highest:
                append_regular_expression(lookup_ascii(lowest).pattern)
                return

            if lowest > highest:
                return

            append_regular_expression(arrange('%s-%s', lookup_ascii(lowest).pattern, lookup_ascii(highest).pattern))


        for i in iterate_range(0, 256):
            if valid[i]:
                if lowest is none:
                    lowest = i
                    continue
            else:
                if lowest is not none:
                    add_range(lowest, i - 1)
                    lowest = none
        else:
            if lowest is not none:
                add_range(lowest, 255)

        append_regular_expression(']')

        portray        = []
        append_portray = portray.append
        many           = []
        append_many    = many.append

        for v in arguments:
            if type(v) is not String:
                append_portray(v.portray)
                append_many   (v)
            else:
                append_portray(portray_string(v))
                append_many   (intern_string (v))

        return RestructureAnyOf(
                   intern_string(''.join(regular_expressions)),
                   intern_arrange('PRINTABLE_MINUS(%s)', ', '.join(portray)),
                   Tuple(many),
               )
    #</PRINTABLE_MINUS>


    @export
    def REPEAT_OR_MORE(pattern, m):
        return create_repeat('REPEAT_OR_MORE', pattern, m, 7777777)


    @export
    def REPEAT(pattern, m, n = none):
        return create_repeat('REPEAT', pattern, m, n)


    def SPECIAL(regular_expression, portray, repeatable = false, singular = false):
        if not repeatable:
            assert not singular

        return RestructureSpecial(intern_string(regular_expression), intern_string(portray), repeatable, singular)


    @export
    def ZERO_OR_MORE(pattern):
        return create_simple_repeat('ZERO_OR_MORE', pattern, '{,7777777}')


    share(
        'name_cache',       name_cache,
    )


    export(
        'BACKSLASH',        SPECIAL(r'\\',          'BACKSLASH',    repeatable = true, singular = true),
        'DOT',              SPECIAL('.',            'DOT',          repeatable = true, singular = true),
        'EMPTY',            SPECIAL('(?#empty)',    'EMPTY'),
        'END_OF_PATTERN',   SPECIAL(r'\Z',          'END_OF_PATTERN'),
        'LINEFEED',         SPECIAL(r'\n',          'LINEFEED',     repeatable = true, singular = true),
        'PRINTABLE',        SPECIAL('[ -~]',        'PRINTABLE',    repeatable = true, singular = true),
    )
