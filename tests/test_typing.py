from __future__ import annotations

import pytest

import pyslang


def test_script_session():
    evaluation = pyslang.ScriptSession()
    assert isinstance(evaluation, pyslang.ScriptSession)

    result = evaluation.eval("8'hFF")
    assert isinstance(result, pyslang.ConstantValue)


@pytest.mark.parametrize("input, expected", [
    ("8'hFF", pyslang.SVInt),
    ("2**8", pyslang.SVInt),
    ("2.0*3'h7", float),
    ("null", pyslang.Null),
    ("$someValue()", None.__class__),
    ("string val = {\"some_str\"}; val", str),
    ("logic [2:0]val = 3'b101; val", pyslang.SVInt),
    ("int val[3] = {1, 2, 3}; val", list),
    ("real val = 3.14; val", float),
])
def test_script_session_output(input, expected):
    evaluation = pyslang.ScriptSession()
    for stmt in input.split(";"):
        result = evaluation.eval(stmt + ";")
    print(result)
    value = result.value
    print(type(value))
    assert isinstance(value, expected)