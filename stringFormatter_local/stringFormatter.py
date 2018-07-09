import time

class Formatter():

    # Makes all characters in string upper case
    def Upper(self, _str):
        print('Upper request received at: %s' % (time.strftime('%H:%M:%S', time.gmtime())))
        return _str.upper()

    # Makes all characters in string lower case
    def Lower(self, _str):
        print('Lower request received at: %s' % (time.strftime('%H:%M:%S', time.gmtime())))
        return _str.lower()

    # Makes first character in each word upper case, all other characters lower case
    def Proper(self, _str):
        print('Proper request received at: %s' % (time.strftime('%H:%M:%S', time.gmtime())))
        return _str.title()


#==================================================
#   GLOBAL VARS
#==================================================
FORMATTER = Formatter()

GET_STR_PROMPT = ('Please insert string to operate:\n')

# All options; keys are numbers, sub dictionary contains titles and functions (via lambda)
OPTIONS ={
    '1': {'title': 'Upper', 'function': (
            lambda string: FORMATTER.Upper(string)
    )},
    '2': {'title': 'Lower', 'function': (
            lambda string: FORMATTER.Lower(string)
    )},
    '3': {'title': 'Capitalize', 'function': (
            lambda string: FORMATTER.Proper(string)
    )}
}


def run():
    # Get input string
    string = str( input(GET_STR_PROMPT) ) # Get value

    print()
    print()

    # Validation loop for getting input
    while True:
        chosenOption = str(input(
            'What would you like to do with the string "%s"?\n%s\n' % ( # Prompt for string
                string,
                ('\n').join([k + ' - ' + v['title'] for k, v in OPTIONS.items()]) # build menu from options
            )
        ))
        if chosenOption in OPTIONS.keys(): # Break if correct option is chosen
            print('Option: %s' % (chosenOption))
            break
        print('This is not a valid option. Please choose from the above.') # Indicate error to user

    sttTime = time.time() # Get time stamp before executing RPC
    rString = OPTIONS[chosenOption]['function'](string) # execute RPC
    endTime = time.time() # Get time after RPC
    print('RESULT: "%s" [%.5f s]' % (rString, endTime - sttTime)) # Print result and time diff

if __name__ == '__main__':
    run()
