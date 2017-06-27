import sqlite3
from os import path as os_path

class Storage():

    def __init__(self):
        pass

    def __init__(self, db_name, db_path, table_name):
        self.db_name = db_name
        self.db_path = db_path
        conn = sqlite3.connect(os_path.join(db_path, db_name))
        cur = conn.cursor()
        try:
            cur.execute("CREATE TABLE {tn}(keyword varchar(20) primary key, emotion varchar(10))".format(tn=table_name))
        except:
            pass
        conn.commit()
        conn.close()

    def create_new_entry(self, table_name, *args):
        try:
            field_list = list(args)
            fields = ", ".join(field_list)
            conn = sqlite3.connect(os_path.join(self.db_path, self.db_name))
            cur = conn.cursor()
            # print "INSERT INTO {tn} VALUES ({fields})".format(tn=table_name, fields=fields)
            cur.execute("INSERT INTO {tn} VALUES ({fields})".format(tn=table_name, fields=fields))
            results = cur.lastrowid
            print results
            conn.commit()
            conn.close()
            return results
        except Exception, e:
            print e
            return None

    def search_for_keyword(self, table_name, keyword):
        try:
            key = "".join(["'", keyword, "'"])
            conn = sqlite3.connect(os_path.join(self.db_path, self.db_name))
            cur = conn.cursor()
            cur.execute("""SELECT * FROM {tn} WHERE keyword={key}""".format(tn=table_name, key=key))
            results = cur.fetchall()
            conn.close()
            return results
        except Exception, e:
            print e
            return None

    def search_for_keyword(self, db_path, db_name, table_name, keyword):
        try:
            key = "".join(["'", keyword, "'"])
            conn = sqlite3.connect(os_path.join(db_path, db_name))
            cur = conn.cursor()
            cur.execute("""SELECT * FROM {tn} WHERE keyword={key}""".format(tn=table_name, key=key))
            results = cur.fetchall()
            conn.close()
            return results
        except Exception, e:
            print e
            return None

    def get_all(self, table_name):
        conn = sqlite3.connect(os_path.join(self.db_path, self.db_name))
        cur = conn.cursor()
        cur.execute("""SELECT * FROM {tn}""".format(tn=table_name))
        results = cur.fetchall()
        conn.close()
        return results
