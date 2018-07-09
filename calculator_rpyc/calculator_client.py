import time
import rpyc


def run():
    conn = rpyc.connect("localhost", 50051)

    # Get inputs for operands
    while True:
        fstOperand = str(input('Please insert first operand:\n')) # Get value
        if fstOperand.isnumeric(): # if valid, break
            fstOperand = float(fstOperand)
            break
        print('Invalid entry: %s, please enter a number' % (fstOperand)) # Err mssg
    while True:
        scdOperand = str(input('Please insert second operand:\n')) # Get value
        if scdOperand.isnumeric(): # If valid, break
            scdOperand = float(scdOperand)
            break
        print('Invalid entry: %s, please enter a number' % (fstOperand)) # Err mssg


    print('1st OPERAND = %f\n2nd OPERAND = %f' % (fstOperand, scdOperand))

    print('======================================================================')

    # Addition
    tm_start = time.time() # Get current time before calling RPC
    result = conn.root.Addition(fstOperand, scdOperand)
    tm_end = time.time() # Get current time after calling RPC
    print('%f + %f = %f [%s]' % (fstOperand, scdOperand, result, tm_end - tm_start)) # print results
    
    # Subtraction
    tm_start = time.time()
    result = conn.root.Subtraction(fstOperand, scdOperand)
    tm_end = time.time()
    print('%f - %f = %f [%s]' % (fstOperand, scdOperand, result, tm_end - tm_start))

    # Multiplication
    tm_start = time.time()
    result = conn.root.Multiplication(fstOperand, scdOperand)
    tm_end = time.time()
    print('%f * %f = %f [%s]' % (fstOperand, scdOperand, result, tm_end - tm_start))

    # Division
    tm_start = time.time()
    result = conn.root.Division(fstOperand, scdOperand)
    tm_end = time.time()
    print('%f / %f = %f [%s]' % (fstOperand, scdOperand, result, tm_end - tm_start))


if __name__ == '__main__':
    run()
