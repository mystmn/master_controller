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
            'c': ['name', 'description']
        }

#    def test_data_creation(self):
    def insert_data(self):

        # 'Create TABLE bob (rowid INTEGER PRIMARY KEY, devices TEXT CHAR (50) NOT NULL)'
        # SELECT `type` FROM `cats`
        # sqlite3 mydatabase.db < db.schema

        try:
            con = sql3.connect(self.config()['db'] + self.config()['file'])

            con.cursor().execute('INSERT INTO {}({},{}) VALUES (?,?)'.format(self.table, "name", "description"),
                                 ("bob", "Gogogog!")
                                 )
            con.commit()
            con.close()
            return "Inserted data successful"

        except:
            return "Failed Migration"

    def select_data(self):

        con = sql3.connect(self.config()['db'] + self.config()['file'])
        c = con.cursor()

        c.execute('SELECT * FROM {}'.format(self.table))
        results = c.fetchall()
        print('1):', len(results))

        con.close()

    def database_confirmation(self, loop=False):

        # print(self.config()['db'])
        # print(os.path.exists(self.config()['db'] + self.config()['file']))

        if not os.path.exists(self.config()['db'] + self.config()['file']):

            if not loop:
                try:
                    os.chdir(self.config()['db'])
                    open(self.config()['file'], "w")

                except:
                    return False

                return self.database_confirmation(True)

            return False

        else:
            return True

    def creation_table(self):
        sc = self.config()['c']

        try:
            con = sql3.connect(self.config()['db'] + self.config()['file'])

            con.cursor().execute(
                'CREATE TABLE if not exists {} (rowid INTEGER PRIMARY KEY, {} TEXT CHAR(50) NOT NULL, '\
                '{} TEXT CHAR(50))'.format(self.table, 'name', 'description')
            )
            con.commit()
            con.close()
            print("Table Confirmed {}".format(self.table))
            return True

        except:
            print("Table wasn't created")
            return False

    def select_table(self, params=(), limit=()):
        s = "SELECT "
        n = "LIMIT "

        with sql3.connect(self.config()['db'] + self.config()['file']) as con:
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
