class Menu(object):
    @staticmethod
    def master_controller_display():
        # nmb = menu selector
        # mes = Message of display
        # com = command to be executed
        return [
            {
                # Consider this a header Message #
                'nmb': 0,
                'Mes': "Please select your scan option\n",
                'com': "Thank you",
            },
            {
                'nmb': 1,
                'Mes': "Cut/Sort all files",
                'com': [
                    "jpg",
                    "html",
                    "doc",
                    "bimp",
                ]
            },
            {
                'nmb': 2,
                'Mes': "Copy/Sort all files",
                'com': [
                    "jpg",
                    "html",
                    "doc",
                    "bimp",
                    "png",
                ]
            },
            {
                'nmb': 3,
                'Mes': "Find OS System",
                'com': "Fire the engines"
            }
        ]


if __name__ == 'menu':
    test = Menu.master_controller_display()
