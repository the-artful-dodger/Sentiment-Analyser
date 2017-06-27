# -*- coding: utf-8 -*-
import pytest
import sqlite3
import hashlib
from src.storage import Storage
from os import path as os_path

@pytest.mark.parametrize("keyword, emotion", [("glad", "happy"),
                                              ("outraged", "angry")])
def test_create_new_entry(tmpdir, keyword, emotion):
    db_path = str(tmpdir.mkdir("database"))
    db_name = "tmp_db"
    stor = Storage(db_name, db_path, "tmp_table")

    kw = "'"+keyword+"'"
    emo = "'"+emotion+"'"
    stor.create_new_entry("tmp_table", kw, emo)

    conn = sqlite3.connect(os_path.join(db_path, db_name))
    cur = conn.cursor()
    # where keyword = ? and emotion = ? , (keyword, emotion)
    entriesMade = cur.execute("select * from tmp_table").fetchall()
    conn.close()
    assert entriesMade == [(keyword, emotion)]

@pytest.mark.parametrize("keyword, emotion", [('dissapointing', 'sad'),
                                              ('provoked', 'angry'),
                                              ('inspired', 'happy'),
                                              pytest.mark.xfail(('ecstatic', 'happy'))])
def test_search_for_key(tmpdir, keyword, emotion):
    db_path = str(tmpdir.mkdir("database"))
    db_name = "tmp_db"
    stor = Storage(db_name, db_path, "tmp_table")

    stor.create_new_entry("tmp_table", "'dissapointing'", "'sad'")
    stor.create_new_entry("tmp_table", "'provoked'", "'angry'")
    stor.create_new_entry("tmp_table", "'inspired'", "'happy'")

    res = stor.search_for_keyword(db_path, db_name, "tmp_table", keyword)

    assert res == [(keyword, emotion)]

def test_get_all(tmpdir):
    db_path = str(tmpdir.mkdir("database"))
    db_name = "tmp_db"
    stor = Storage(db_name, db_path, "tmp_table")

    stor.create_new_entry("tmp_table", "'dissapointing'", "'sad'")
    stor.create_new_entry("tmp_table", "'provoked'", "'angry'")
    stor.create_new_entry("tmp_table", "'inspired'", "'happy'")
    stor.create_new_entry("tmp_table", "'offended'", "'angry'")
    stor.create_new_entry("tmp_table", "'pleased'", "'happy'")

    res = stor.get_all("tmp_table")

    assert res == [('dissapointing', 'sad'), ('provoked', 'angry'), ('inspired', 'happy'), ('offended', 'angry'), ('pleased', 'happy')]