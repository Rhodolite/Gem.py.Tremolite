#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('TremoliteParser.Parse')
def module():
    require_module('TremoliteParser.Core')
    require_module('TremoliteParser.Parse1')


    @share
    def parse_tremolite(path, show = 0, test = 0):
        #line("parse_tremolite(path<%s>, show<%d>, test<%d>)", path, show, test);

        [data, data_lines, data_many] = parse_tremolite_from_path(path)

        tree_many = data_many

        if test is 7:
            test_identical_output(path, data, data_many, tree_many)
            test_count_newlines(data_lines, tree_many)

        return data_many
