# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import grpc
import time

# RPC modules
import calculator_pb2
import calculator_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    calc = calculator_pb2_grpc.CalculatorStub(channel)

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
    result = calc.Addition(calculator_pb2.AdditionRequest(fstOperandAdd=fstOperand, scdOperandAdd=scdOperand)).resultAdd
    tm_end = time.time() # Get current time after calling RPC
    print('%f + %f = %f [%s]' % (fstOperand, scdOperand, result, tm_end - tm_start)) # print results
    
    # Subtraction
    tm_start = time.time()
    result = calc.Subtraction(calculator_pb2.SubtractionRequest(fstOperandSub=fstOperand, scdOperandSub=scdOperand)).resultSub
    tm_end = time.time()
    print('%f - %f = %f [%s]' % (fstOperand, scdOperand, result, tm_end - tm_start))

    # Multiplication
    tm_start = time.time()
    result = calc.Multiplication(calculator_pb2.MultiplicationRequest(fstOperandMul=fstOperand, scdOperandMul=scdOperand)).resultMul
    tm_end = time.time()
    print('%f * %f = %f [%s]' % (fstOperand, scdOperand, result, tm_end - tm_start))

    # Division
    tm_start = time.time()
    result = calc.Division(calculator_pb2.DivisionRequest(fstOperandDiv=fstOperand, scdOperandDiv=scdOperand)).resultDiv
    tm_end = time.time()
    print('%f / %f = %f [%s]' % (fstOperand, scdOperand, result, tm_end - tm_start))


if __name__ == '__main__':
    run()
