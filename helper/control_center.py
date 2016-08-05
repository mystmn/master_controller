import helper, subprocess

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

    def main_station(self):

        s = self.display()

        print("{} finished".format(s))

        return False

    def display(self, x=False, msg=False):
        print(msg)
        for each in helper.Menu.master_controller_display():

            if each['nmb'] == 0:
                print('{}'.format(each['Mes']))

            else:
                if x:
                    if x == each['nmb']:
                        return each['com']
                    else:
                        msg = "{} isn't optional".format(x)
                print('{}) {}'.format(each['nmb'], each['Mes']))

        if msg is not False:
            print('\n** {} **'.format(msg))

        x = input("\nWhich option would you like > ")

        return self.filter_int(x)

    def filter_int(self, x):
        try:
            if int(x):
                return self.display(int(x))
        except:
            return self.display(False, "Ths following is not numerical '{}'...try again.".format(x))

    def validate_int(self, x):
        try:
            int(x)
            return int(x)
        except ValueError:
            return False
