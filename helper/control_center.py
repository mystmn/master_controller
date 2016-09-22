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

        devices = model.DbController("devices")

        if not devices.database_confirmation():
            exit("Unable to create file in the requested location")

        if devices.creation_table():
            print(devices.insert_data())
            print(devices.select_data())

        else:
            print("This application is broken...")
            print(devices.test_creation_table())

        return False
