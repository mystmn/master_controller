# https://github.com/dbader/schedule/blob/master/FAQ.rst
import helper
import model

'''
# Created by Paul Cameron
'''
print("** {} **\n".format(model.definition()['ProjectName']))
print("** {} **".format(model.definition()['ProjectPurpose']))

while True:
    if model.definition()['Schedule']:
        pass

    else:
        hc = helper.Controller()

        if not hc.station():
            exit()

        else:
            pass

print("Script has ended")

# email.conn() McAfee is blocking the required ports
