# -*- encoding: utf-8 -*-
# Author: li_colin

# import pytest


class TestParser:
    @staticmethod
    def test_regex_findall_variables():
        from pipeline_runner import regex_findall_variables
        assert regex_findall_variables("$$") == []
        assert regex_findall_variables("$a$b$c") == ["a", "b", "c"]
        assert regex_findall_variables("$a$1$c") == ["a", "c"]
