import helper, model

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

        devices = model.DbController("devices")

        if not devices.table_confirm_exist():
            exit("Unable to create file in the requested location")

        if devices.table_creation()[0]:
            print(devices.table_insert())
            print(devices.table_select())

        else:
            print("This application is broken...")
            print(devices.test_creation_table())

        return False
