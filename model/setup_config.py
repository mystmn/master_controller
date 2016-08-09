import model
import sqlite3 as sql


class DbController(object):
    def __init__(self, table):
        self.table = table

    @staticmethod
    def setup_beta():
        return {
            'db': r'{}{}'.format(model.definition()['Root'], "\model\main.db"),
            'limit': 20,  # Default Limit
            'desc': 'ORDER BY {} DESC'.format('id'),  # SELECT * FROM tablename ORDER BY column DESC LIMIT 1;
        }

    def table_creation(self, x=()):
        try:
            with sql.connect(self.setup_beta()['db']) as con:
                data = 'CREATE TABLE {} (email, username, phone, password)'.format(self.table)
                con.cursor().execute(data)
                con.commit()
                con.close()
            return [True, "Created Table, {}".format(data)]
        except:
            return [False, "Table wasn't created"]

    def insert_account_holder(self, email="bob", username="bob", phone="bob", password="bob"):
            with sql.connect(self.setup_beta()['db']) as con:

                con.cursor().execute("INSERT INTO {}(email,username,phone,password) VALUES (?,?,?,?)"\
                           .format(self.table), (email, username, phone, password))
                con.commit()
            con.close()

    def select_account_holder(self, params=(), limit=()):
        s = "SELECT "
        n = "LIMIT "

        with sql.connect(self.setup_beta()['db']) as con:
            cur = con.cursor()

            if params == ():
                # result = cur.execute("SELECT * FROM {}".format(TABLE, limit))
                s += "* FROM "
            else:
                s += "{} FROM ".format(params)

            if limit == ():
                s += "{} {}".format(str(self.table), n + str(self.setup_beta['limit']))
            else:
                s += "{} {}".format(str(self.table), n + str(limit))

            result = cur.execute(s).fetchall()

        con.close()
        return result
