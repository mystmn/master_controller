import helper, model, sqlite3

'''
Things to make
1) Scan for Models
2) Scan for Bundles
3) Send Bundle Modifications
4) Office Usage
5) Scheduled Task
6) Send popups via web based
7) Make HTML layout
'''


class Controller(object):
    def __init__(self):
        pass

    @staticmethod
    def station():
        s = helper.display()
        print("{} finished".format(s))

        cows = model.DbController("cows")
        cows.table_creation()
        print(cows.insert_account_holder())

        return False
