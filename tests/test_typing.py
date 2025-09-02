from __future__ import annotations


import pyslang


def test_script_session():
    evaluation = pyslang.ScriptSession()
    assert isinstance(evaluation, pyslang.ScriptSession)

    result = evaluation.eval("8'hFF")
    assert isinstance(result, pyslang.ConstantValue)
