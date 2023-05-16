# -*- encoding: utf-8 -*-
# Author: li_colin

# import pytest

import re
# "\$\{([a-zA-Z_]\w*)"  function name
#
function_match = re.compile(r"\$\{([a-zA-Z_]\w*\()")


class TestParser:
    @staticmethod
    def test_regex_findall_variables():
        from pipeline_runner import regex_findall_variables
        assert regex_findall_variables("$$") == []
        assert regex_findall_variables("$a$b$c") == ["a", "b", "c"]
        assert regex_findall_variables("$a$1$c") == ["a", "c"]

    def test_regex_findall_functions(self):
        from pipeline_runner import regex_findall_functions
        print("xxx functions ", regex_findall_functions("${func(5)}"))
        print("yyy functions ", regex_findall_functions("${func(a=1, b=2)}"))
