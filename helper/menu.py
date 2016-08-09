import helper


def master_controller_display():
    # nmb = menu selector
    # mes = Message of display
    # com = command to be executed
    return [
        {
            # Consider this a header Message #
            'nmb': "a",
            'Mes': "Welcome, please select your scan option\n",
        },
        {
            'nmb': 1,
            'Mes': "scan for models",
            'com': [
                "jpg",
                "html",
                "doc",
                "bimp",
            ]
        },
        {
            'nmb': 2,
            'Mes': "ultimate",
            'com': [
                "jpg",
                "html",
                "doc",
                "bimp",
                "png",
            ]
        },
        {
            'nmb': 9,
            'Mes': "run setup",
            'com': "Firing the engines"
        }
    ]


def display(x=False, msg=False):
    for each in master_controller_display():

        if each['nmb'] == "a":
            #helper.cls()
            print('{}'.format(each['Mes']))
        else:
            print('{}) {}'.format(each['nmb'], each['Mes']))
            if x:
                if x == each['nmb']:
                    return each['com']
                else:
                    msg = "{} isn't optional".format(x)

    if msg is not False:
        print('\n** {} **'.format(msg))

    x = input("\nWhich option would you like > ")

    return filter_int(x)


def filter_int(x):
    try:
        if int(x):
            return display(int(x))
        elif str(x):
            return display(False, "Ths following is not a valid choice '{}'.".format(x))
        else:
            pass
    except:
        return display(False, "Ths following is not numerical '{}'.".format(x))
