import model
import sqlite3 as sql3


class DbController(object):
    def __init__(self, table):
        self.table = table

    @staticmethod
    def config():
        return {
            'db': r'{}{}'.format(model.definition()['Root'], "\model\main.db"),
            'limit': 20,  # Default Limit
            'desc': 'ORDER BY {} DESC'.format('id'),  # SELECT * FROM tablename ORDER BY column DESC LIMIT 1;
            'c': ['name_device', 'ip_device', 'model_device', 'user_device', 'stamp']
        }

    def test_creation_table(self):
        sc = self.config()['c']
        print(self.config()['db'])

            # 'Create TABLE bob (rowid INTEGER PRIMARY KEY, devices TEXT CHAR (50) NOT NULL)'
            # SELECT `type` FROM `cats`

        con = sql3.connect(self.config()['db'])
        cursor = con.cursor().execute('SELECT `type` FROM `{}` '.format('cats'))
        print(cursor.fetchall())
        con.close()

    def table_creation(self):
        sc = self.config()['c']

        try:
            with sql3.connect(self.config()['db']) as con:
                con.cur = 'CREATE TABLE {} (' \
                       'rowid INTEGER PRIMARY KEY, ' \
                       '{} TEXT CHAR(50) NOT NULL, ' \
                       '{} TEXT CHAR(50), ' \
                       '{} TEXT CHAR(50), ' \
                       '{} TEXT CHAR(50), ' \
                       '{} CURRENT_TIMESTAMP' \
                       ')' \
                    .format(self.table, sc[0], sc[1], sc[2], sc[3])
                con.cursor().execute(data)
                con.commit()
                con.close()
            return [True, "Created Table, {}".format(data)]
        except:
            return [False, "Table wasn't created, it may already exist"]

    def table_insert(self, a="", b="", c="", d="", e=""):
        sc = self.config()['c']

        with sql3.connect(self.config()['db']) as con:
            con.cursor().execute("INSERT INTO {}({},{},{},{}, {}) VALUES (?,?,?,?,? )" \
                                 .format(self.table, sc[0], sc[1], sc[2], sc[3], sc[4]), (a, b, c, d, e))
            con.commit()
        con.close()
        return [True, "Data Inserted, {}, {}, {},{}".format(a, b, c, d)]

    def table_select(self, params=(), limit=()):
        s = "SELECT "
        n = "LIMIT "

        with sql.connect(self.config()['db']) as con:
            cur = con.cursor()

            if params == ():
                # result = cur.execute("SELECT * FROM {}".format(TABLE, limit))
                s += "* FROM "
            else:
                s += "{} FROM ".format(params)

            if limit == ():
                s += "{} {}".format(str(self.table), n + str(self.config()['limit']))
            else:
                s += "{} {}".format(str(self.table), n + str(limit))

            result = cur.execute(s).fetchall()

        con.close()
        return result
