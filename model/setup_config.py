import model, os
import sqlite3 as sql3


class DbController(object):
    def __init__(self, table):
        self.table = table

    @staticmethod
    def config():
        return {
            'db': r'{}{}'.format(model.definition()['Root'], "/model/"),
            'file': "main.db",
            'limit': 20,  # Default Limit
            'desc': 'ORDER BY {} DESC'.format('id'),  # SELECT * FROM tablename ORDER BY column DESC LIMIT 1;
            'c': ['name_device', 'ip_device', 'model_device', 'user_device', 'stamp']
        }

    def test_creation_table(self):
        sc = self.config()['c']
        print(self.config()['db'])

        # 'Create TABLE bob (rowid INTEGER PRIMARY KEY, devices TEXT CHAR (50) NOT NULL)'
        # SELECT `type` FROM `cats`
        # sqlite3 mydatabase.db < db.schema
        try:
            con = sql3.connect(self.config()['db'] + self.config()['file'])

            con.cursor().execute('INSERT INTO {}({},{}) VALUES (?,?)'.format("project", "name", "description"),
                                 ("pacmans", "Gogogog!")
                                 )
            con.commit()
            con.close()
            return "Inserted data successful"

        except:
            return "Failed Migration"

        # cursor = con.cursor().execute('SELECT `name` FROM `{}` '.format('project'))
        # print(cursor.fetchall())
        # con.close()

    def test_insert_data(self):
        con = sql3.connect(self.config()['db'] + self.config()['file'])
        cursor = con.cursor().execute("INSERT INTO {}({},{},{},{}, {}) VALUES (?,?,?,?,? )" \
                                      .format(self.table, sc[0], sc[1], sc[2], sc[3], sc[4]), (a, b, c, d, e)
                                      )
        con.commit()
        con.close()

    def table_confirm_exist(self, loop=False):

        # print(self.config()['db'])
        # print(os.path.exists(self.config()['db'] + self.config()['file']))

        if not os.path.exists(self.config()['db'] + self.config()['file']):

            if not loop:
                try:
                    os.chdir(self.config()['db'])
                    open(self.config()['file'], "w")

                except:
                    return False

                return self.table_confirm_exist(True)

            return False

        else:
            return True

    def table_creation(self):
        sc = self.config()['c']

        try:
            with sql3.connect(self.config()['db'] + self.config()['file']) as con:
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
