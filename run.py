# https://github.com/dbader/schedule/blob/master/FAQ.rst
import helper, model

'''
# Created by Paul Cameron
'''
print("** {} **\n".format(model.config.definition['ProjectName']))
print("** {} **".format(model.config.definition['ProjectPurpose']))

while True:
    if model.config.definition['Schedule']:
        pass

    else:
        hc = helper.Controller()

        if not hc.main_station():
            exit()

        else:
            pass

print("Script has ended")

# email.conn() McAfee is blocking the required ports
