#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('TremoliteParser.Tokenize1Atom')
def module():
    #
    #   Note:
    #       See note in "PythonParser.Token1Atom" on the need to use `==` instead of `is` when comparing `i & `j`
    #
    #   Note #2:
    #       The previous note also applies to tests like `qi() != j` ... cannot replace this with `qi() is not j`.
    #
    @share
    def analyze_atom(m):
        if m.start('newline') is -1:
            quote_start = m.start('quote')

            if quote_start is not -1:
                j         = qj()
                quote_end = m.end('quote')

                if qi() != j:
                    r = find_evoke_whitespace_atom(qs()[quote_start])(j, quote_end)
                else:
                    s = qs()

                    r = find_atom_type(s[quote_start])(s[j : quote_end])

                wi(quote_end)
                wj(m.end())

                return r

            raise_unknown_line()

        #
        #   Newline
        #
        quote_start = m.start('quote')

        if quote_start is not -1:
            #
            #   NOTE:
            #
            #       In the code below: Use 'qj()' instead of "m.start('quote')" to be sure to pick up any letters
            #       prefixing the quote, such as r'prefixed'
            #

            #
            #<similiar-to: {atom_s} above>
            #
            #   Differences:
            #
            #       Uses "quote_end" instead of "m.end('atom')"
            #       Uses "s" intead of "qs()"
            #
            if qd() is not 0:
                if qi() == qj():
                    r = find_evoke_atom_whitespace(qs()[quote_start])(m.end('quote'), none)
                else:
                    r = find_evoke_whitespace_atom_whitespace(qs()[quote_start])(qj(), m.end('quote'), none)

                skip_tokenize_prefix()

                return r

            j         = qj()
            quote_end = m.end('quote')
            s         = qs()

            if qi() == qj():
                r = find_atom_type(s[quote_start])(s[j : quote_end])
            else:
                r = find_evoke_whitespace_atom(s[quote_start])(j, quote_end)

            wn(conjure_line_marker(s[m.end('quote') : ]))

            return r
            #</similiar-to>

        raise_unknown_line()
