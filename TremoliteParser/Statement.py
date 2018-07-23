#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('TremoliteParser.Statement')
def gem():
    require_gem('TremoliteParser.Core')
    require_gem('TremoliteParser.Tree')


    class LanguagePattern(TremoliteParserTrunk):
        __slots__ = ((
            'frill',                    #   VW_Frill | Commented_VW_Frill
            'keyword_language',         #   KeywordLanguage+
            'keyword_pattern',          #   KeywordPattern+
        ))


        is_herd      = false
        is_statement = true


        def __init__(t, frill, keyword_language, keyword_pattern):
            t.frill            = frill
            t.keyword_language = keyword_language
            t.keyword_pattern  = keyword_pattern


        def __repr__(t):
            return arrange('<%s %r %r %r>', t.__class__.__name__, t.frill, t.keyword_language, t.keyword_pattern)


        def count_newlines(t):
            return t.frill.count_newlines() + t.keyword_language.count_newlines() + t.keyword_pattern.count_newlines()


        def display_token(t):
            frill = t.frill

            return arrange('<language-pattern +%d%s %s %s>',
                           frill.v.total,
                           t.keyword_language.display_token(),
                           t.keyword_pattern .display_token(),
                           frill.w           .display_token());


        def dump_token(t, f, newline = true):
            frill = t.frill
            
            f.partial('<language-pattern +%d ', frill.v.total)

            t.keyword_language.dump_token(f)
            t.keyword_pattern .dump_token(f)
            r = frill.w       .dump_token(f, false)

            return f.token_result(r, newline)


        #order = order__frill_ab


        def write(t, w):
            frill = t.frill

            w(frill.v.s)
            t.keyword_language.write(w)
            t.keyword_pattern .write(w)
            w(frill.w.s)


    LanguagePattern.frill = LanguagePattern.frill
    LanguagePattern.a     = LanguagePattern.keyword_language
    LanguagePattern.b     = LanguagePattern.keyword_pattern

    LanguagePattern.k1 = LanguagePattern.frill
    LanguagePattern.k2 = LanguagePattern.keyword_language
    LanguagePattern.k3 = LanguagePattern.keyword_pattern


    def produce_conjure_language_pattern_statement(name, meta):
        cache = create_cache(name, conjure_nub)

        return produce_conjure_unique_triple__312(name, meta, cache)


    conjure_language_pattern_statement = produce_conjure_language_pattern_statement(
            'language-pattern',
            LanguagePattern,
        )


    export(
        'conjure_language_pattern_statement',   conjure_language_pattern_statement,
    )
