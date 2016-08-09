import os


def definition():
    return {
        'ProjectName': "Project Master Blaster has begun",
        'ProjectPurpose': "This script was created to scan a network for information",
        'Schedule': False,
        'Menu': False,
        'Logs': True,
        'Root': os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '')),
    }
