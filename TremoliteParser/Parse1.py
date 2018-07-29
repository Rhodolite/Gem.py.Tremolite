#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('TremoliteParser.Parse1')
def module():
    require_module('TremoliteParser.Elemental')
    require_module('TremoliteParser.Match')
    require_module('TremoliteParser.Statement')
    require_module('TremoliteParser.Tokenize1Atom')
    require_module('TremoliteParser.DualExpressionStatement')


    def parse_tremolite_statement_pattern(m):
        if m.end('newline') != -1:
            raise_unknown_line()

        j = m.end()
        s = qs()

        indentation_end  = m.end('indented')
        name_end         = m.end('name')
        colon_equal_end  = m.end('colon_equal')

        indentation = conjure_indentation(s[                : indentation_end])
        name        = conjure_name       (s[indentation_end : name_end])
        colon_equal = conjure_colon_equal(s[name_end        : j])

        wi(j)
        wj(j)

        #
        #   <atom>
        #
        m = atom_match(s, j)

        if m is none:
            raise_unknown_line()

        atom = analyze_atom(m)
        newline = qn()

        if newline is none:
            raise_unknown_line()

        return conjure_pattern_statement(indentation, name, colon_equal, atom, newline)

        
    def parse_tremolite_statement_language(m):
        if m.end('newline') != -1:
            raise_unknown_line()

        j = m.end()
        s = qs()

        indentation_end  = m.end('indented')
        indentation      = conjure_indentation(s[ :  indentation_end])
        keyword_language = conjure_keyword_language(s[indentation_end : j])

        wi(j)
        wj(j)


        #
        #<pattern>
        #
        m = language_pattern_match(s, j)

        if m is none:
            raise_unknown_line()

        pattern_end     = m.end('pattern')
        keyword_pattern = conjure_keyword_pattern(s[j            : pattern_end])
        newline         = conjure_line_marker    (s[ pattern_end : ])

        j = m.end()

        wi(j)
        wj(j)
        #</name>

        return conjure_language_pattern_statement(
                conjure_vw_frill(indentation, newline),
                keyword_language,
                keyword_pattern,
            )


    lookup_parse_tremolite_line = {
                                      'language' : parse_tremolite_statement_language,
                                  }.get


    @share
    def parse_tremolite_from_path(path):
        data = read_text_from_path(path)

        parse_context = z_initialize(path, data)

        append        = parse_context.append
        many          = parse_context.many
        iterate_lines = parse_context.iterate_lines

        for LOOP in parse_context:
            with parse_context:
                for s in iterate_lines:
                    #line('s: %s', s)

                    m = line_match(s)

                    if m is none:
                        raise_unknown_line()

                    keyword_s = m.group('keyword')

                    if keyword_s is not none:
                        parse1_line = lookup_parse_tremolite_line(keyword_s)

                        if parse1_line is not none:
                            append(parse1_line(m))

                            continue

                        raise_unknown_line()

                    name_s = m.group('name')

                    if name_s is not none:
                        append(parse_tremolite_statement_pattern(m))

                        assert qd() is 0
                        continue

                    comment_end = m.end('comment')

                    if comment_end is not -1:
                        append(conjure_any_comment_line(m.end('indented'), comment_end))
                        continue

                    if m.end('newline') is -1:
                        raise_unknown_line()

                    append(conjure_empty_line(m.group()))

        return ((data, parse_context.data_lines, many))
