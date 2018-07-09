from __future__ import print_function

import grpc
import time

# RPC modules
import stringFormatter_pb2
import stringFormatter_pb2_grpc

#==============================================================================
#                                  GLOBAL VARS
#==============================================================================
CHANNEL = grpc.insecure_channel('localhost:50051')
FORMATTER = stringFormatter_pb2_grpc.StringFormatterStub(CHANNEL)

GET_STR_PROMPT = ('Please insert string to operate:\n')

# All options; keys are numbers, sub dictionary contains titles and functions (via lambda)
OPTIONS ={
    '1': {'title': 'Upper', 'function': (
            lambda string: FORMATTER.Upper( stringFormatter_pb2.UpperRequest( upperReqStr=string ) ).upperRepStr
            )},
    '2': {'title': 'Lower', 'function': (
            lambda string: FORMATTER.Lower( stringFormatter_pb2.LowerRequest( lowerReqStr=string) ).lowerRepStr
    )},
    '3': {'title': 'Capitalize', 'function': (
            lambda string: FORMATTER.Proper( stringFormatter_pb2.ProperRequest( propReqStr=string) ).propRepStr
    )}
}

#==============================================================================
#                                     MAIN
#==============================================================================
def run():
    # Get input string
    string = str(input(GET_STR_PROMPT)) # Get value

    print()
    print(  )

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
