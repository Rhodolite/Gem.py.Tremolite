#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('Rex.PatternWrapper')
def gem():
    require_gem('Rex.Core')


    show = true


    class MatchWrapper(Object):
        __slots__ = ((
            'name',                     #   String+
            'pattern_groups',           #   Tuple of (None | String+)
            'wrapped',                  #   SRE_Match
            'end',                      #   Method
            'group',                    #   Method
            'groups',                   #   Method
            'start',                    #   Method
        ))


        def __init__(t, name, pattern_groups, wrapped):
            t.name           = name
            t.pattern_groups = pattern_groups
            t.wrapped        = wrapped

            t.end    = wrapped.end
            t.group  = wrapped.group
            t.groups = wrapped.groups
            t.start  = wrapped.start


        def __repr__(t):
            group          = t.group
            pattern_groups = t.pattern_groups

            if length(pattern_groups) is 1:
                return arrange('<Match %s %s>', t.name, portray_string(group(0)))

            if length(pattern_groups) is 2:
                group_1 = group(1)

                return arrange('<Match %s %s %s=%s>',
                               t.name, portray_string(group(0)), pattern_groups[1],
                               'none'   if group_1 is none else   portray_string(group_1))

            many   = []
            append = many.append

            for s in pattern_groups:
                if s is none:
                    continue

                v = group(s)

                if v is none:
                    append(arrange('%s=none', s))
                    continue

                append(arrange('%s=%s', s, portray_string(v)))


            return arrange('<Match %s %s %s>', t.name, portray_string(t.group(0)), ' '.join(many))


        def portray_match(t):
            group           = t.group
            pattern_groups  = t.pattern_groups
            portray_group_0 = portray_string(group(0))

            if pattern_groups is 0:
                return portray_group_0

            if length(pattern_groups) is 2:
                group_1 = group(1)

                return arrange('%s %s=%s',
                               portray_group_0,
                               pattern_groups[1],
                               'none'   if group_1 is none else   portray_string(group_1))

            many   = [portray_group_0]
            append = many.append

            for s in pattern_groups:
                if s is none:
                    continue

                v = group(s)

                if v is none:
                    append(arrange('%s=none', s))
                    continue

                append(arrange('%s=%s', s, portray_string(v)))

            return ' '.join(many)


    @export
    class PatternWrapper(Object):
        __slots__ = ((
            'name',                     #   String+
            'pattern_groups',           #   Tuple of (None | String+)
            'wrapped',                  #   SRE_Pattern
        ))


        def __init__(t, name, pattern_groups, wrapped):
            t.name           = name
            t.pattern_groups = pattern_groups
            t.wrapped        = wrapped


        def __repr__(t):
            return arrange('<PatternWrapper %s>', t.name)


        if show:
            def match(t, s, index = absent):
                if index is absent:
                    m = t.wrapped.match(s)
                else:
                    m = t.wrapped.match(s, index)

                if m is none:
                    if index is absent:
                        line('%s(%s) => none', t.name, portray_string(s))
                    else:
                        line('%s(%s @%d %s) => none', t.name, portray_string(s[:index]), index, portray_string(s[index:]))

                    return none

                r = MatchWrapper(t.name, t.pattern_groups, m)

                if index is absent:
                    line('%s(%s)', t.name, portray_string(s))
                else:
                    line('%s(%s @%d %s)', t.name, portray_string(s[:index]), index, portray_string(s[index:]))

                line('  => %s', r.portray_match())

                return r
        else:
            def match(t, s, index = absent):
                if index is absent:
                    m = t.wrapped.match(s)
                else:
                    m = t.wrapped.match(s, index)

                if m is none:
                    return none

                return MatchWrapper(t.name, t.pattern_groups, m)


    @export
    def create_wrapped_match_function(name, regular_expression, code, groups, flags):
        return PatternWrapper(name, groups, compile_regular_expression(regular_expression, code, groups, flags)).match
