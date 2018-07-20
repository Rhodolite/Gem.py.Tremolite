#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('Tremolite_2.Parse1')
def gem():
    require_gem('Tremolite_2.Core')
    require_gem('Tremolite_2.Match')


    def parse_java_statement_import(m):
        j = m.end()
        s = qs()

        if m.end('newline') == -1:
            keyword = conjure_keyword_import(s[:j])
        else:
            keyword = conjure_keyword_import__ends_in_newline(s[:j])

        wi(j)
        wj(j)


        #
        #<name>
        #
        m = name_match(s, qj())

        if m is none:
            raise_unknown_line()

        package = conjure_name(m.group())

        j = m.end()

        wi(j)
        wj(j)
        #</name>

        line('keyword: %s; package: %s', keyword, package)

        raise_unknown_line()


    lookup_parse_java_line = {
                                 'import' : parse_java_statement_import,
                             }.get


    @share
    def parse_java_from_path(path):
        data = read_text_from_path(path)

        parse_context = z_initialize(path, data)

        append        = parse_context.append
        many          = parse_context.many
        iterate_lines = parse_context.iterate_lines

        for LOOP in parse_context:
            with parse_context:
                for s in iterate_lines:
                    line('s: %s', s)

                    m = line_match(s)

                    if m is none:
                        raise_unknown_line()

                    keyword_s = m.group('keyword')

                    if keyword_s is not none:
                        parse1_line = lookup_parse_java_line(keyword_s)

                        if parse1_line is not none:
                            append(parse1_line(m))

                            continue

                        raise_unknown_line()

                    raise_unknown_line()

                    comment_end = m.end('comment')

                    if comment_end is not -1:
                        append(conjure_any_comment_line(m.end('indented'), comment_end))
                        continue

                    if m.end('newline') is -1:
                        raise_unknown_line()

                    append(conjure_empty_line(m.group()))

        return ((data, parse_context.data_lines, many))
