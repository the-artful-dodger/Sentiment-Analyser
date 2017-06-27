# -*- coding: utf-8 -*-
import pytest
import sqlite3
import hashlib
from src.storage import Storage
from src.analyser import Analyser
from os import path as os_path

@pytest.mark.parametrize("with_punc, wo_punc", [(["Hello, how are you"], ['hello', 'how', 'are', 'you']),
                                                (["There's a fire, call the fire-department!!"], ['theres', 'a', 'fire', 'call', 'the', 'firedepartment']),
                                                pytest.mark.xfail((["I, don't think this'll work."], ['I,', 'dont', 'think', 'thisll', 'work']))])
def test_remove_punctuation(with_punc, wo_punc):
    anl = Analyser()
    res = anl.remove_punctuation(with_punc)
    assert res == wo_punc


def test_analyse_emotion(monkeypatch):

    monkeypatch.setattr(Storage, '__init__', lambda x: None)
    #monkeypatch.setattr(a, 'search_for_keyword', keyword_search)
    anl = Analyser()
    res = anl.analyse_emotion(["This is a string"])

    assert res == (0, 0, 0)